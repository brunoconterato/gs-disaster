import sys
import os
from datetime import datetime, timedelta
import json

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.database_session import get_db_connection, release_db_connection, SessionLocal
from predictor_notifier.fake_alert import create_fake_alert
from predictor_notifier.notifier import notify_alert, check_alert_webhook_credentials
from ml.ml_utils import (
    load_and_process_data_from_db,
    prepare_timeseries_data,
    load_model,
    get_scaler,
    denormalize_column,
    predict,
    MODELS_PATH,
)


def main():
    check_alert_webhook_credentials()

    conn = get_db_connection()
    print("Successfully connected to the database!")

    db = SessionLocal()

    # Load hyperparameters
    hyperparams_path = os.path.join(MODELS_PATH, "lstm_hyperparams.json")
    if os.path.exists(hyperparams_path):
        with open(hyperparams_path, "r") as f:
            hyperparams = json.load(f)
            sequence_length = hyperparams.get("sequence_length", 5)
    else:
        hyperparams = {}
        sequence_length = 5
    print(f"Hyperparameters: {hyperparams}")

    # TODO: get data from db
    # You can adjust these dates as needed or make them dynamic
    end_date = datetime.today().strftime("%Y-%m-%d")
    start_date = (datetime.today() - timedelta(days=sequence_length)).strftime(
        "%Y-%m-%d"
    )
    example_data = load_and_process_data_from_db(
        start_date=start_date, end_date=end_date
    )
    print(f"Loaded example data from DB: {example_data.shape}")

    dataset, scaler, processed_data = prepare_timeseries_data(
        example_data,
        sequence_length=sequence_length,
        target_col="level_downstream_max",
    )

    # Load Model
    if dataset is not None and len(dataset) > 0:
        input_size = dataset[0][0].shape[1]
        model, hyperparams = load_model("lstm.pt", "LSTM", sample_input=dataset[0][0])
    else:
        input_size = None
        model, hyperparams = load_model("lstm.pt", "LSTM", input_size=input_size)
    print(f"Loaded model: {model}, Hyperparams: {hyperparams}")

    if dataset is not None and len(dataset) > 0:
        scaler = get_scaler(scaler)
        unscaled_seq = denormalize_column(
            scaler, processed_data, "level_downstream_max"
        )
        print("Input sequence for prediction (level_downstream_max):")
        print(unscaled_seq)
        prediction = predict(model, processed_data, hyperparams, scaler=scaler)
        print(f"Prediction: {prediction}")
    else:
        print("No data available for the specified date range.")
        prediction = None

    # TODO: save prediction to db

    # TODO: save alert to db if prediction is greater than threshold
    
    # TODO: notify alert if prediction is greater than threshold

    db.close()
    release_db_connection(conn)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        raise e
