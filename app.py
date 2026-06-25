import streamlit as st
import pandas as pd

st.title("EcoWatch AI")

try:
    df = pd.read_csv(
        "data/raw/environment_data.csv"
    )

    st.dataframe(df)

except:
    st.warning("No data collected")