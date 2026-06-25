import streamlit as st
import pandas as pd

st.header(
    "Forecast"
)

df = pd.read_csv(
    "data/raw/environment_data.csv"
)

st.line_chart(
    df["aqi"]
)