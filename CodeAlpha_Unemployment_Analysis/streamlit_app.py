import streamlit as st
from PIL import Image

st.title("📊 Unemployment Analysis Dashboard")

st.write(
"""
This dashboard presents an analysis of unemployment trends in India,
including regional patterns, COVID-19 impact, and seasonal trends.
"""
)

option = st.sidebar.selectbox(
"Select Analysis",
[
"Unemployment Trend",
"Average Unemployment by Region",
"Distribution of Unemployment",
"Labour Participation vs Unemployment",
"Covid Impact",
"Monthly Pattern",
"Regional Heatmap"
]
)

if option == "Unemployment Trend":
    st.header("Unemployment Trend Over Time")
    st.image("images/unemployment_trend.png")

elif option == "Average Unemployment by Region":
    st.header("Average Unemployment Rate by Region")
    st.image("images/region_unemployment.png")

elif option == "Distribution of Unemployment":
    st.header("Distribution of Unemployment Rates")
    st.image("images/distribution.png")

elif option == "Labour Participation vs Unemployment":
    st.header("Labour Participation vs Unemployment Rate")
    st.image("images/participation_vs_unemployment.png")

elif option == "Covid Impact":
    st.header("Unemployment Before and During COVID-19")
    st.image("images/covid_comparison.png")

elif option == "Monthly Pattern":
    st.header("Seasonal / Monthly Unemployment Pattern")
    st.image("images/monthly_pattern.png")

elif option == "Regional Heatmap":
    st.header("Regional Heatmap of Unemployment")
    st.image("images/unemployment_heatmap.png")