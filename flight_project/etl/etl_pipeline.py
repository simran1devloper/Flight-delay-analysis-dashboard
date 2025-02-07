from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, unix_timestamp
import requests
import pandas as pd

# Initialize Spark session
spark = SparkSession.builder.appName("FlightDelayETL").getOrCreate()

# Load historical flight data
flight_data = spark.read.csv("flight_data.csv", header=True, inferSchema=True)

# Fetch real-time weather and air traffic data
def fetch_weather(airport_code):
    api_key = "YOUR_API_KEY"
    url = f"https://api.weather.com/v3/wx/conditions/current?airport={airport_code}&apiKey={api_key}"
    response = requests.get(url)
    return response.json()

# Sample function for air traffic API
def fetch_air_traffic(airport_code):
    api_key = "YOUR_API_KEY"
    url = f"https://api.traffic.com/airport/{airport_code}?apiKey={api_key}"
    response = requests.get(url)
    return response.json()

# Data Cleaning
flight_data = flight_data.withColumn("scheduled_departure", to_timestamp(col("scheduled_departure")))
flight_data = flight_data.withColumn("actual_departure", to_timestamp(col("actual_departure")))
flight_data = flight_data.withColumn("delay", (unix_timestamp(col("actual_departure")) - unix_timestamp(col("scheduled_departure"))) / 60)

# Save processed data
flight_data.write.csv("processed_flight_data.csv", header=True)
