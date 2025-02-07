import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Load processed data
df = pd.read_csv("processed_flight_data.csv")

# Feature Engineering
features = ["weather_conditions", "air_traffic", "scheduled_hour", "day_of_week", "season"]
X = df[features]
y = df["delay"].apply(lambda x: 1 if x > 15 else 0)  # Binary classification: Delayed (>15 mins) or not

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# XGBoost Model
xgb_model = xgb.XGBClassifier()
xgb_model.fit(X_train, y_train)
xgb_preds = xgb_model.predict(X_test)
print(f"XGBoost Accuracy: {accuracy_score(y_test, xgb_preds)}")

# Random Forest Model
rf_model = RandomForestClassifier(n_estimators=100)
rf_model.fit(X_train, y_train)
rf_preds = rf_model.predict(X_test)
print(f"Random Forest Accuracy: {accuracy_score(y_test, rf_preds)}")

# LSTM Model
X_train_lstm = X_train.values.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test_lstm = X_test.values.reshape(X_test.shape[0], X_test.shape[1], 1)

lstm_model = Sequential([
    LSTM(50, activation='relu', input_shape=(X_train.shape[1], 1)),
    Dense(1, activation='sigmoid')
])

lstm_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
lstm_model.fit(X_train_lstm, y_train, epochs=10, batch_size=32)
lstm_preds = (lstm_model.predict(X_test_lstm) > 0.5).astype("int32")

print(f"LSTM Accuracy: {accuracy_score(y_test, lstm_preds)}")

# Save models
xgb_model.save_model("xgb_model.json")
rf_model.fit(X_train, y_train)  # Retrain before saving
import joblib
joblib.dump(rf_model, "rf_model.pkl")
lstm_model.save("lstm_model.h5")
