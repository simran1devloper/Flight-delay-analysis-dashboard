import React from "react";
import FlightDelayPredictor from "./components/FlightDelayPredictor";

function App() {
  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <div className="bg-white p-6 rounded-xl shadow-lg w-full max-w-3xl">
        <h1 className="text-2xl font-bold text-center mb-4">Flight Delay Prediction</h1>
        <FlightDelayPredictor />
      </div>
    </div>
  );
}

export default App;
