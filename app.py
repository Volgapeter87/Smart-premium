import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("smartpremium_model.pkl")

st.set_page_config(page_title="SmartPremium", layout="centered")

st.title("💰 SmartPremium: Insurance Cost Predictor")
st.write("Enter customer details to predict insurance premium")

# ---------------------------
# USER INPUTS
# ---------------------------
age = st.slider("Age", 18, 80, 30)
gender = st.selectbox("Gender", ["Male", "Female"])
income = st.number_input("Annual Income", min_value=10000, step=1000)
marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
dependents = st.number_input("Number of Dependents", 0, 10)
education = st.selectbox("Education Level", ["High School", "Bachelor's", "Master's", "PhD"])
occupation = st.selectbox("Occupation", ["Employed", "Self-Employed", "Unemployed"])
health_score = st.slider("Health Score", 0, 100, 60)
location = st.selectbox("Location", ["Urban", "Suburban", "Rural"])
policy_type = st.selectbox("Policy Type", ["Basic", "Comprehensive", "Premium"])
previous_claims = st.number_input("Previous Claims", 0, 10)
vehicle_age = st.number_input("Vehicle Age", 0, 30)
credit_score = st.number_input("Credit Score", 300, 900)
insurance_duration = st.number_input("Insurance Duration (Years)", 1, 30)
smoking = st.selectbox("Smoking Status", ["Yes", "No"])
exercise = st.selectbox("Exercise Frequency", ["Daily", "Weekly", "Monthly", "Rarely"])
property_type = st.selectbox("Property Type", ["House", "Apartment", "Condo"])

# ---------------------------
# PREDICTION
# ---------------------------
if st.button("Predict Premium 💰"):

    input_data = pd.DataFrame({
        "Age": [age],
        "Gender": [gender],
        "Annual Income": [income],
        "Marital Status": [marital_status],
        "Number of Dependents": [dependents],
        "Education Level": [education],
        "Occupation": [occupation],
        "Health Score": [health_score],
        "Location": [location],
        "Policy Type": [policy_type],
        "Previous Claims": [previous_claims],
        "Vehicle Age": [vehicle_age],
        "Credit Score": [credit_score],
        "Insurance Duration": [insurance_duration],
        "Smoking Status": [smoking],
        "Exercise Frequency": [exercise],
        "Property Type": [property_type]
    })

    prediction = model.predict(input_data)[0]

    st.success(f"💰 Estimated Insurance Premium: ₹ {prediction:,.2f}")
