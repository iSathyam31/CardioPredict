import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
with open('heart.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to make predictions
def predict_heart_attack(features):
    prediction = model.predict([features])
    return prediction[0]

# Streamlit app
st.title("Heart Attack Prediction")

# Collect user input
age = st.number_input("Age", min_value=1, max_value=120, value=25)
sex = st.selectbox("Sex", [0, 1])
cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
trtbps = st.number_input("Resting Blood Pressure (in mm Hg)", min_value=50, max_value=200, value=120)
chol = st.number_input("Cholesterol (in mg/dl)", min_value=100, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
restecg = st.selectbox("Resting Electrocardiographic Results", [0, 1, 2])
thalachh = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220, value=150)
exng = st.selectbox("Exercise Induced Angina", [0, 1])
caa = st.selectbox("Number of Major Vessels Colored by Flourosopy", [0, 1, 2, 3, 4])

# Prepare features for prediction
features = [age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, caa]

# Predict button
if st.button("Predict"):
    prediction = predict_heart_attack(features)
    if prediction == 1:
        st.write("The model predicts that you have a heart disease.")
    else:
        st.write("The model predicts that you do not have a heart disease.")


