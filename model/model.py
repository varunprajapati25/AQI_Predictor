import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import pickle

# Load dataset
df = pd.read_csv("../data/aqi_data.csv")

# Features (input)
X = df[['PM2.5', 'PM10', 'NO2', 'SO2', 'NH3', 'CO', 'OZONE']]

# Target (output)
y = df['AQI']

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
print("MAE:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Save model
import os
os.makedirs("model", exist_ok=True)
pickle.dump(model, open("aqi_model.pkl", "wb"))

print("Model trained and saved!")
