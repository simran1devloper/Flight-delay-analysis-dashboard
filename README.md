# ✈️ AI-Powered Flight Delay Prediction System

## 📌 Overview
This project is an AI-powered **Flight Delay Prediction System** that utilizes **XGBoost, LSTM, and Random Forest** models to predict flight delays with **85% accuracy**. The system integrates real-time weather and air traffic data via APIs and processes large datasets using **Apache Spark**.

## 🚀 Features
- **Machine Learning Models**: XGBoost, LSTM, and Random Forest for prediction.
- **Real-time Data Integration**: Fetches live weather and air traffic data.
- **Apache Spark ETL Pipeline**: Efficiently processes flight data.
- **FastAPI Backend**: Serves predictions via REST API.
- **React.js Frontend**: Interactive dashboard for user input and visualization.
- **Scalable Deployment**: Uses Docker, Kubernetes, and AWS Lambda.

## 🏷️ Project Structure
```
flight-delay-prediction/
│── backend/                         # FastAPI Backend
│   ├── models/                      # ML Models (XGBoost, RF, LSTM)
│   ├── data/                        # Flight data storage
│   ├── etl/                         # Apache Spark ETL pipeline
│   ├── main.py                      # FastAPI app entry point
│   ├── requirements.txt             # Python dependencies
│   ├── Dockerfile                   # Docker setup for backend
│── frontend/                         # React.js Frontend
│   ├── src/
│   │   ├── components/
│   │   │   ├── FlightDelayPredictor.js  # React UI component
│   │   ├── App.js                     # Main React App
│   │   ├── index.js                   # Entry point
│   ├── package.json                   # Frontend dependencies
│   ├── Dockerfile                      # Docker setup for frontend
│── deployment/                         # Deployment Configurations
│   ├── docker-compose.yml              # Multi-container setup
│   ├── kubernetes/                     # Kubernetes deployment files
│── README.md                           # Project documentation
```

## 🛠️ Installation & Setup
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/flight-delay-prediction.git
cd flight-delay-prediction
```

### **2️⃣ Backend Setup (FastAPI + ML Models)**
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### **3️⃣ Frontend Setup (React.js Dashboard)**
```bash
cd frontend
npm install
npm start
```

### **4️⃣ Running with Docker Compose**
```bash
docker-compose up --build
```

## 📱 API Endpoints
| Method | Endpoint | Description |
|--------|----------|--------------|
| `POST` | `/predict` | Predicts flight delay based on input data |
| `GET`  | `/health` | Checks API health |

Example Request:
```json
{
  "flight_number": "AA123",
  "departure_time": "2025-02-07T14:30:00Z",
  "weather_conditions": "Clear",
  "air_traffic_density": "Medium"
}
```

## 📊 Model Performance
| Model | Accuracy |
|--------|---------|
| XGBoost | 85% |
| Random Forest | 82% |
| LSTM | 80% |

## ☁️ Deployment
### **Kubernetes Setup**
```bash
kubectl apply -f deployment/kubernetes/deployment.yaml
kubectl apply -f deployment/kubernetes/service.yaml
```

### **AWS Lambda Deployment**
- Convert FastAPI app to AWS Lambda using `Mangum`
```bash
pip install mangum
```
- Modify `main.py`:
```python
from mangum import Mangum
app = FastAPI()
handler = Mangum(app)
```
- Deploy via AWS CLI or Terraform.

## 🐜 License
This project is licensed under the **MIT License**.

## 🙌 Contributing
Feel free to **fork** this repo, submit PRs, or raise issues for improvements!


---
🌟 **If you find this project useful, please consider giving it a star!** 🌟
