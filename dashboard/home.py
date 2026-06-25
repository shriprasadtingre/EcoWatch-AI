import streamlit as st
import pandas as pd

df = pd.read_csv(
    "data/raw/environment_data.csv"
)

st.header(
    "Environmental Dashboard"
)

st.dataframe(df.tail())