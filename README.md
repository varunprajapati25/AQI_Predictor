# 🌫️ AQI Predictor using Machine Learning

## 📌 Project Overview
Air pollution has become one of the most serious environmental and public health challenges in recent years. Rapid industrialization, urbanization, and increasing vehicular emissions have significantly contributed to poor air quality. The *Air Quality Index (AQI)* is a standardized measure used to indicate how polluted the air is and how it may affect human health.

This project aims to develop a *Machine Learning-based AQI Predictor* that estimates AQI values using pollutant concentrations such as *PM2.5, PM10, NO2, SO2, NH3, CO,* and *Ozone*. The system uses a trained model and allows users to input values through the terminal to get predicted AQI instantly.

---

## 🎯 Problem Statement
The objective of this project is to build a system that can accurately *predict AQI values* based on pollutant data. In real-world scenarios, AQI depends on multiple environmental factors, and calculating it manually can be complex.

This project simplifies the process by using machine learning to automatically learn relationships between pollutants and AQI. The system takes pollutant values as input and outputs a numerical AQI value, making it useful for quick analysis and decision-making.

---

## 🚀 Solution
To solve this problem, a *Random Forest Regression model* is used. This model is trained on a dataset containing pollutant values and corresponding AQI values.

The model learns patterns and relationships between input features and the AQI. Once trained, it can predict AQI for new data entered by the user. The prediction is performed using a simple terminal-based interface, making the system easy to use and efficient.

---

## 🛠️ Tech Stack
- *Programming Language:* Python  
- *Libraries Used:*  
  - pandas (data handling)  
  - numpy (numerical operations)  
  - scikit-learn (machine learning)  
- *Model:* Random Forest Regressor  
- *Interface:* Command Line (Terminal-based)



---

## 📂 Project Structure
aqi-predictor/
│── data/
│ └── aqi_data.csv
│
│── model/
│ ├── model.py
│ └── aqi_model.pkl
│
│── predict.py
│── README.md


---

## ⚙️ Installation & Setup

### 1. Clone the Repository


### 2. Install Dependencies


---

## ▶️ How to Run the Project

### Step 1: Train the Model

*This will train the model and generate `aqi_model.pkl`.*

---

### Step 2: Run Prediction


---

### Step 3: Enter Input Values
Example:
PM2.5: 50
PM10: 100
NO2: 30
SO2: 10
NH3: 5
CO: 2
OZONE: 40


---

### Step 4: Output

Predicted AQI: 120.45


---

## 📊 Features
- Predicts *exact AQI value* using regression  
- Uses multiple pollutant parameters  
- Simple terminal-based interface  
- Fast and efficient prediction system  

---

## 📈 Methodology
The project follows a structured machine learning workflow:
1. Load and explore dataset  
2. Data preprocessing and cleaning  
3. Feature selection (PM2.5, PM10, etc.)  
4. Split data into training and testing sets  
5. Train model using Random Forest Regression  
6. Evaluate model using MAE and R² Score  
7. Save trained model using pickle  
8. Use model for prediction via terminal input  

---

## 📊 Results
The trained model successfully predicts AQI values based on pollutant inputs. The performance is evaluated using metrics like Mean Absolute Error and R² Score, showing that the model can reasonably approximate AQI values.

Although predictions may not be perfectly accurate due to real-world variations, they provide a close estimation, demonstrating the effectiveness of machine learning in environmental data analysis.

---

## ⚠️ Limitations
- Model accuracy depends on dataset quality  
- Does not include weather factors like temperature or humidity  
- Predictions are approximate, not exact real-world AQI  
- Limited dataset may reduce generalization  

---

## 🔮 Future Improvements
- Integrate real-time data using APIs  
- Add weather parameters for better accuracy  
- Develop a GUI or web application  
- Use advanced models like XGBoost or Deep Learning  

---


---

## ⭐ Acknowledgement
This project is developed for academic purposes to demonstrate the use of Machine Learning in solving real-world environmental problems like air quality prediction.
