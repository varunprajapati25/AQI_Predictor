import pickle
import numpy as np

# Load model
model = pickle.load(open("model/aqi_model.pkl", "rb"))

print("Enter values:")

pm25 = float(input("PM2.5: "))
pm10 = float(input("PM10: "))
no2 = float(input("NO2: "))
so2 = float(input("SO2: "))
nh3 = float(input("NH3: "))
co = float(input("CO: "))
ozone = float(input("OZONE: "))

import pandas as pd
data = pd.DataFrame([{
    'PM2.5': pm25,
    'PM10': pm10,
    'NO2': no2,
    'SO2': so2,
    'NH3': nh3,
    'CO': co,
    'OZONE': ozone
}])

prediction = model.predict(data)
print(f"Predicted AQI: {round(prediction[0], 2)}")
