import streamlit as st
from PIL import Image

st.title("Car Price Prediction Analysis")

st.write(
"""
This project builds a machine learning regression model to predict car prices
based on vehicle features.
"""
)

option = st.sidebar.selectbox(
"Select Visualization",
[
"Model Prediction Plot"
]
)

if option == "Model Prediction Plot":
    st.header("Actual vs Predicted Car Prices")
    st.image("images/prediction_plot.png")