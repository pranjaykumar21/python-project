import streamlit as st
import numpy as np
import pandas as pd

# Set page config
st.set_page_config(
    page_title="Crop Prediction",
    page_icon="🌱",
    layout="centered"
)

# Custom CSS for dark theme and styling
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: white;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 24px;
        border-radius: 5px;
    }
    .main {
        background-image: url('https://images.unsplash.com/photo-1587095951604-b9d924a3fda0');
        background-size: cover;
    }
    h1 {
        color: white;
        text-align: center;
        padding: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Navigation menu
menu = ["Home", "Predict", "Visualize", "Products", "About"]
st.markdown("""
<div style='text-align: center; padding: 10px;'>
    <span style='margin: 0 10px;'>Home</span>
    <span style='margin: 0 10px;'>Predict</span>
    <span style='margin: 0 10px;'>Visualize</span>
    <span style='margin: 0 10px;'>Products</span>
    <span style='margin: 0 10px;'>About</span>
</div>
""", unsafe_allow_html=True)

# Title
st.title("CROP PREDICTION")

# Create a form for input
with st.form("prediction_form"):
    # Input fields
    state = st.selectbox("State", ["Andhra Pradesh", "Karnataka", "Tamil Nadu", "Kerala", "Other"])
    rainfall = st.number_input("Rainfall", min_value=0.0, max_value=1000.0, value=100.0)
    season = st.selectbox("Season", ["Kharif", "Rabi", "Whole Year"])
    temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0)
    soil_type = st.selectbox("Soil Type", ["Black", "Red", "Sandy", "Loamy", "Clay"])
    season_type = st.selectbox("Season Type", ["Humid", "Dry", "Normal"])
    crop = st.selectbox("Crop", ["Paddy", "Wheat", "Sugarcane", "Cotton", "Maize"])

    # Submit button
    submitted = st.form_submit_button("Predict")

# Prediction logic
if submitted:
    # Create a card-like display for results
    st.markdown("""
        <div style='background-color: rgba(255, 255, 255, 0.1); 
                    padding: 20px; 
                    border-radius: 10px; 
                    margin-top: 20px;'>
            <h3 style='text-align: center; color: #4CAF50;'>Prediction Results</h3>
            <table style='width: 100%; margin-top: 20px;'>
                <tr>
                    <td style='padding: 10px;'>State:</td>
                    <td style='padding: 10px;'>{}</td>
                </tr>
                <tr>
                    <td style='padding: 10px;'>Rainfall:</td>
                    <td style='padding: 10px;'>{} mm</td>
                </tr>
                <tr>
                    <td style='padding: 10px;'>Temperature:</td>
                    <td style='padding: 10px;'>{} °C</td>
                </tr>
                <tr>
                    <td style='padding: 10px;'>Soil Type:</td>
                    <td style='padding: 10px;'>{}</td>
                </tr>
                <tr>
                    <td style='padding: 10px;'>Season:</td>
                    <td style='padding: 10px;'>{}</td>
                </tr>
                <tr>
                    <td style='padding: 10px;'>Recommended Crop:</td>
                    <td style='padding: 10px; color: #4CAF50; font-weight: bold;'>{}</td>
                </tr>
            </table>
        </div>
    """.format(state, rainfall, temperature, soil_type, season, crop), unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style='position: fixed; 
                bottom: 0; 
                left: 0; 
                width: 100%; 
                background-color: rgba(0,0,0,0.7); 
                padding: 10px; 
                text-align: center;'>
        © 2024 Crop Prediction System. All rights reserved.
    </div>
    """, unsafe_allow_html=True) 