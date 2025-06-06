import json
import torch
import pandas as pd
import numpy as np
from typing import Any, Dict, Optional
from torch.utils.data import Dataset

# Add the parent directory to the system path to import custom modules
import sys
import os
from sklearn.preprocessing import StandardScaler
import joblib

# Ensure the project root is in sys.path for module imports
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f"Project root resolved to: {project_root}")  # Debug print
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from ml.models import MLP, LSTM, GRU
from ml.data_process import load_and_process_data_from_db


MODELS_PATH = os.path.join(project_root, "models")
print("Models path:", MODELS_PATH)  # Debug: print models path

MODEL_CLASSES = {
    "MLP": MLP,
    "LSTM": LSTM,
    "GRU": GRU,
}


def load_model(
    filename: str, model_type: str, sample_input=None, input_size=None
) -> tuple:
    """
    Loads a model and its hyperparameters from the models/ folder.
    Always uses input_size from hyperparams (must be saved during training).
    Returns (model, hyperparams)
    """
    model_type = model_type.upper()
    pt_path = os.path.join(MODELS_PATH, filename)
    print("Loading model from:", pt_path)  # Debug: print model path
    json_path = os.path.join(MODELS_PATH, f"{model_type.lower()}_hyperparams.json")
    with open(json_path, "r") as f:
        hyperparams = json.load(f)
    ModelClass = MODEL_CLASSES[model_type]
    # Always get input_size from hyperparams
    input_size = hyperparams.get("input_size", None)
    if input_size is None:
        raise ValueError(
            "input_size not found in hyperparams. Please ensure it is saved during model training."
        )
    print("Input size for model:", input_size)  # Debug: print input size
    if model_type == "MLP":
        model = ModelClass(
            input_size=input_size,
            hidden_layers=hyperparams["hidden_layers"],
            learning_rate=hyperparams["learning_rate"],
        )
    elif model_type in ["LSTM", "GRU"]:
        model = ModelClass(
            input_size=input_size,
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
        assert (
            len(self.data) >= self.sequence_length
        ), "Not enough data for the given sequence length."

    def __len__(self):
        return len(self.data) - self.sequence_length

    def __getitem__(self, idx):
        x = self.data.iloc[
            idx : idx + self.sequence_length
        ].values  # (sequence_length, num_features)
        # Label is the value of target_col for the next day after the sequence
        y = self.data.iloc[idx + self.sequence_length, self.target_col]  # next day
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
    df = df.reset_index(drop=True)

    # Remove columns containing 'flow' if requested
    if drop_flow:
        df = df.loc[:, ~df.columns.str.contains("flow")]
    # Normalize all columns except 'date_sin' and 'date_cos' (if present)
    cols_to_normalize = [
        col for col in df.columns if col not in ["date_sin", "date_cos"]
    ]
    scaler = get_scaler(scaler)
    df[cols_to_normalize] = scaler.transform(df[cols_to_normalize])
    dataset = TimeSeriesDataset(
        df, sequence_length=sequence_length, target_col=target_col
    )
    return dataset, scaler, df


def get_data_from_db(
    start_date=None,
    end_date=None,
    sequence_length=5,
    target_col="level_downstream_max",
    drop_flow=True,
    scaler=None,
):
    """
    Fetches data from the database using load_and_process_data_from_db,
    preprocesses it (removes flow columns, normalizes, etc.), and returns a TimeSeriesDataset ready for inference.
    """
    # Ignore db_session and limit, as load_and_process_data_from_db manages its own session and loads all data in range
    df = load_and_process_data_from_db(start_date=start_date, end_date=end_date)

    print(df.columns)  # Debug: print column names
    print(df.head())  # Debug: print first few rows of the DataFrame

    dataset, scaler, df = prepare_timeseries_data(
        df,
        sequence_length=sequence_length,
        target_col=target_col,
        drop_flow=drop_flow,
        scaler=scaler,
    )
    return dataset, scaler, df


def predict(
    model,
    data: pd.DataFrame,
    hyperparams: Dict[str, Any],
    scaler=None,
):
    """
    Runs predictions using the loaded model and the provided data.
    If data length == sequence_length, returns a single prediction.
    If data length > sequence_length, returns a list of predictions (sliding window).
    All predictions are denormalized to the original scale.
    """
    sequence_length = hyperparams.get("sequence_length", 5)
    target_col = hyperparams.get("target_col", "level_downstream_max")
    # Remove columns containing 'flow' if present (to match training)
    data = data.loc[:, ~data.columns.str.contains("flow")]
    # Normalize all columns except 'date_sin' and 'date_cos' (if present)
    cols_to_normalize = [
        col for col in data.columns if col not in ["date_sin", "date_cos"]
    ]
    scaler = get_scaler(scaler)
    data[cols_to_normalize] = scaler.transform(data[cols_to_normalize])

    if len(data) < sequence_length:
        raise ValueError(
            f"Not enough data for sequence length {sequence_length}. Data length: {len(data)}"
        )

    model.eval()
    preds = []
    with torch.no_grad():
        # Sliding window prediction
        for i in range(len(data) - sequence_length + 1):
            window = data.iloc[i : i + sequence_length].values
            x = torch.tensor(window, dtype=torch.float32)
            x = x.unsqueeze(0)  # (1, sequence_length, num_features)
            pred = model(x)
            if hasattr(pred, "item"):
                pred = pred.item()
            else:
                pred = float(pred.squeeze().cpu().numpy())
            preds.append(pred)
    # Denormalize all predictions
    unscaled_preds = denormalize_column(scaler, data, target_col, values=preds)
    return unscaled_preds.tolist() if len(unscaled_preds) > 1 else unscaled_preds[0]


def denormalize_column(scaler, data, column, values=None, last_n=None):
    """
    Denormalizes a single column from normalized data using the provided scaler.
    If values is provided, denormalizes those values; otherwise, uses the last_n rows from data[column].
    Returns a numpy array of denormalized values.
    """
    cols_to_normalize = [
        col for col in data.columns if col not in ["date_sin", "date_cos"]
    ]
    target_idx = data.columns.get_loc(column)
    if values is not None:
        arr = np.array(values)
        arr = arr.reshape(-1)
        dummy = np.zeros((arr.shape[0], len(cols_to_normalize)))
        dummy[:, target_idx] = arr
    elif last_n is not None:
        arr = data[column].iloc[-last_n:].values
        dummy = np.zeros((last_n, len(cols_to_normalize)))
        dummy[:, target_idx] = arr
    else:
        arr = data[column].values
        dummy = np.zeros((arr.shape[0], len(cols_to_normalize)))
        dummy[:, target_idx] = arr
    unscaled = scaler.inverse_transform(dummy)
    return unscaled[:, target_idx]


if __name__ == "__main__":
    # Load a small range of data from the database (replace with your desired dates)
    example_data = load_and_process_data_from_db(
        start_date="2024-02-01", end_date="2024-02-04"
    )
    print(f"Loaded example data from DB: {example_data.shape}")

    if os.path.exists(os.path.join(MODELS_PATH, "mlp_hyperparams.json")):
        with open(os.path.join(MODELS_PATH, "mlp_hyperparams.json"), "r") as f:
            hyperparams = json.load(f)
            sequence_length = hyperparams.get("sequence_length", 5)
    print(f"Hyperparameters: {hyperparams}")
    dataset, scaler, processed_data = prepare_timeseries_data(
        example_data,
        sequence_length=sequence_length,
        target_col="level_downstream_max",
    )
    # Infer input_size from dataset (if available), similar to the notebook
    print("Dataset:", dataset.data)
    if dataset is not None:
        print(f"Dataset length: {len(dataset)}")
    else:
        print("Dataset length: 0")
    if dataset is not None and len(dataset) > 0:
        input_size = dataset[0][0].shape[1]
        print(f"Inferred input_size from dataset: {input_size}")
        # Pass a sample_input to load_model to ensure correct input_size
        model, hyperparams = load_model("mlp.pt", "MLP", sample_input=dataset[0][0])
    else:
        input_size = None
        model, hyperparams = load_model("mlp.pt", "MLP", input_size=input_size)
    print(f"Loaded model: {model}, Hyperparams: {hyperparams}")

    if dataset is not None:
        # Print the sequence for the prediction column used as input (denormalized)
        print("Input sequence for prediction (level_downstream_max):")
        scaler = get_scaler(scaler)
        unscaled_seq = denormalize_column(
            scaler, processed_data, "level_downstream_max"
        )
        print(unscaled_seq)
        prediction = predict(model, processed_data, hyperparams, scaler=scaler)
        print(f"Prediction: {prediction}")
    else:
        print("No data available for the specified date range.")
