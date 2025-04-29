import streamlit as st
import numpy as np
import pickle

# Load the trained model and scalers
model = pickle.load(open('model.pkl', 'rb'))
standscaler = pickle.load(open('standscaler.pkl', 'rb'))
minmaxscaler = pickle.load(open('minmaxscaler.pkl', 'rb'))

# Streamlit app title
st.title("🌾 Crop Recommendation System")

# Input fields for user to enter soil and environmental parameters
N = st.number_input("Nitrogen (N)", min_value=0, max_value=140, value=50)
P = st.number_input("Phosphorus (P)", min_value=5, max_value=145, value=50)
K = st.number_input("Potassium (K)", min_value=5, max_value=205, value=50)
temperature = st.number_input("Temperature (°C)", min_value=10.0, max_value=45.0, value=25.0)
humidity = st.number_input("Humidity (%)", min_value=10.0, max_value=100.0, value=50.0)
ph = st.number_input("pH", min_value=3.5, max_value=9.5, value=6.5)
rainfall = st.number_input("Rainfall (mm)", min_value=20.0, max_value=300.0, value=100.0)

# Predict button
if st.button("Predict Suitable Crop"):
    # Prepare the input data
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    # Apply the same scaling as during model training
    input_data_scaled = standscaler.transform(input_data)
    input_data_scaled = minmaxscaler.transform(input_data_scaled)
    # Make prediction
    prediction = model.predict(input_data_scaled)
    # Display the result
    st.success(f"🌱 The recommended crop is: {prediction[0]}")
