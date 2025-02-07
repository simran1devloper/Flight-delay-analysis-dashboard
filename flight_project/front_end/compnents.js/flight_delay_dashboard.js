import React, { useState } from "react";
import axios from "axios";

function FlightDelayPredictor() {
  const [data, setData] = useState({});
  const [inputs, setInputs] = useState({
    weather_conditions: 0,
    air_traffic: 0,
    scheduled_hour: 0,
    day_of_week: 0,
    season: 0,
  });

  const handleChange = (e) => {
    setInputs({ ...inputs, [e.target.name]: parseFloat(e.target.value) });
  };

  const handleSubmit = async () => {
    const response = await axios.post("http://localhost:8000/predict", inputs);
    setData(response.data);
  };

  return (
    <div>
      <h1>Flight Delay Predictor</h1>
      <input type="number" name="weather_conditions" onChange={handleChange} />
      <input type="number" name="air_traffic" onChange={handleChange} />
      <input type="number" name="scheduled_hour" onChange={handleChange} />
      <input type="number" name="day_of_week" onChange={handleChange} />
      <input type="number" name="season" onChange={handleChange} />
      <button onClick={handleSubmit}>Predict</button>
      <p>XGBoost: {data.XGBoost}</p>
      <p>Random Forest: {data.RandomForest}</p>
      <p>LSTM: {data.LSTM}</p>
    </div>
  );
}

export default FlightDelayPredictor;
