from fastapi import FastAPI
import xgboost as xgb
import joblib
import tensorflow as tf
import numpy as np
import pandas as pd

app = FastAPI()

# Load models
xgb_model = xgb.XGBClassifier()
xgb_model.load_model("xgb_model.json")
rf_model = joblib.load("rf_model.pkl")
lstm_model = tf.keras.models.load_model("lstm_model.h5")

@app.post("/predict")
def predict_flight_delay(weather_conditions: float, air_traffic: float, scheduled_hour: int, day_of_week: int, season: int):
    features = np.array([[weather_conditions, air_traffic, scheduled_hour, day_of_week, season]])

    xgb_pred = xgb_model.predict(features)[0]
    rf_pred = rf_model.predict(features)[0]

    lstm_features = features.reshape(1, features.shape[1], 1)
    lstm_pred = (lstm_model.predict(lstm_features) > 0.5).astype("int32")[0][0]

    return {"XGBoost": int(xgb_pred), "Random Forest": int(rf_pred), "LSTM": int(lstm_pred)}

# Run server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
