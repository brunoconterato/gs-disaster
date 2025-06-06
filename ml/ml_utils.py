import os
import json
import torch
import pandas as pd
from typing import Any, Dict
from torch.utils.data import Dataset
from db.database_session import SessionLocal
from db.crud import get_resampled_measurements_daily
from ml.models import MLP, LSTM, GRU  # Import models from models.py
from sklearn.preprocessing import StandardScaler
import joblib

MODELS_PATH = os.path.join(os.path.dirname(__file__), "../models")

MODEL_CLASSES = {
    "MLP": MLP,
    "LSTM": LSTM,
    "GRU": GRU,
}


def load_model(model_type: str):
    """
    Loads a model and its hyperparameters from the models/ folder.
    Returns (model, hyperparams)
    """
    model_type = model_type.upper()
    pt_path = os.path.join(MODELS_PATH, f"{model_type.lower()}.pt")
    json_path = os.path.join(MODELS_PATH, f"{model_type.lower()}_hyperparams.json")
    with open(json_path, "r") as f:
        hyperparams = json.load(f)
    ModelClass = MODEL_CLASSES[model_type]
    # Remove None values for kwargs
    model_kwargs = {
        k: v
        for k, v in hyperparams.items()
        if k not in ["model_type", "batch_size", "sequence_length"] and v is not None
    }
    # For MLP, need input_size (user must provide or infer from data)
    # Here, we set input_size=hyperparams.get('input_size', 1) as a placeholder
    if model_type == "MLP":
        model = ModelClass(
            input_size=hyperparams.get("input_size", 1),
            hidden_layers=hyperparams["hidden_layers"],
            learning_rate=hyperparams["learning_rate"],
        )
    elif model_type in ["LSTM", "GRU"]:
        model = ModelClass(
            input_size=hyperparams.get("input_size", 1),
            hidden_size=hyperparams["hidden_size"],
            num_layers=hyperparams["num_layers"],
            learning_rate=hyperparams["learning_rate"],
        )
    else:
        raise ValueError(f"Unknown model type: {model_type}")
    model.load_state_dict(torch.load(pt_path, map_location="cpu"))
    model.eval()
    return model, hyperparams


class TimeSeriesDataset(Dataset):
    def __init__(self, data, sequence_length=24, target_col="level_downstream_max"):
        self.data = data.reset_index(drop=True)
        self.sequence_length = sequence_length
        self.target_col = self.data.columns.get_loc(target_col)

    def __len__(self):
        return len(self.data) - self.sequence_length

    def __getitem__(self, idx):
        x = self.data.iloc[
            idx : idx + self.sequence_length
        ].values  # (sequence_length, num_features)
        y = self.data.iloc[idx + self.sequence_length, self.target_col]  # scalar value
        return torch.tensor(x, dtype=torch.float32), torch.tensor(
            y, dtype=torch.float32
        )


def get_scaler(scaler=None):
    """
    Loads or creates a StandardScaler for the dataset.
    """
    scaler_path = os.path.join(MODELS_PATH, "scaler.save")
    if scaler is not None:
        return scaler
    if os.path.exists(scaler_path):
        return joblib.load(scaler_path)
    return StandardScaler()


def prepare_timeseries_data(
    df: pd.DataFrame,
    sequence_length=5,
    target_col="level_downstream_max",
    drop_flow=True,
    scaler=None,
):
    """
    Preprocesses the DataFrame: removes flow columns, normalizes, and returns a TimeSeriesDataset.
    """
    if df.empty:
        return None, scaler, df
    df = df.set_index("date")
    # Remove columns containing 'flow' if requested
    if drop_flow:
        df = df.loc[:, ~df.columns.str.contains("flow")]
    # Normalize all columns except 'date_sin' and 'date_cos' (if present)
    cols_to_normalize = [
        col for col in df.columns if col not in ["date_sin", "date_cos"]
    ]
    scaler = get_scaler(scaler)
    if not hasattr(scaler, "mean_"):
        df[cols_to_normalize] = scaler.fit_transform(df[cols_to_normalize])
    else:
        df[cols_to_normalize] = scaler.transform(df[cols_to_normalize])
    dataset = TimeSeriesDataset(
        df, sequence_length=sequence_length, target_col=target_col
    )
    return dataset, scaler, df


def get_data_from_db(
    db_session=None,
    start_date=None,
    end_date=None,
    limit=1000,
    sequence_length=5,
    target_col="level_downstream_max",
    drop_flow=True,
    scaler=None,
):
    """
    Fetches data from the resampled_measurements_daily view using db.crud.get_resampled_measurements_daily,
    preprocesses it (removes flow columns, normalizes, etc.), and returns a TimeSeriesDataset ready for inference.
    """
    if db_session is None:
        db_session = SessionLocal()
        close_session = True
    else:
        close_session = False
    try:
        rows = get_resampled_measurements_daily(db_session, start_date, end_date, limit)
        df = pd.DataFrame(rows, columns=rows[0].keys() if rows else [])
        dataset, scaler, df = prepare_timeseries_data(
            df,
            sequence_length=sequence_length,
            target_col=target_col,
            drop_flow=drop_flow,
            scaler=scaler,
        )
        return dataset, scaler, df
    finally:
        if close_session:
            db_session.close()


def predict(
    model,
    data: pd.DataFrame,
    hyperparams: Dict[str, Any],
    target_col="level_downstream_max",
):
    """
    Runs predictions using the loaded model and the provided data.
    Uses the correct window size (sequence_length) from hyperparams.
    Returns a list of predictions (aligned with data index, None for first N rows).
    """
    sequence_length = hyperparams.get("sequence_length", 5)
    # Exclude the target column from inputs
    input_cols = [col for col in data.columns if col != target_col]
    preds = [None] * len(data)
    model.eval()
    with torch.no_grad():
        for i in range(len(data) - sequence_length):
            x = data.iloc[i : i + sequence_length][input_cols].values
            x_tensor = torch.tensor(x, dtype=torch.float32).unsqueeze(0)
            y_pred = model(x_tensor).cpu().numpy().squeeze()
            preds[i + sequence_length] = float(y_pred)
    return preds
