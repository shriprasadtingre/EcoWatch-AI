import streamlit as st
import pandas as pd
from prediction.health_index import calculate_ehi

st.title("EcoWatch AI")

try:
    df = pd.read_csv(
        "data/raw/environment_data.csv"
    )

    latest = df.iloc[-1]

    score, status = calculate_ehi(
        latest["temperature"],
        latest["humidity"],
        latest["wind_speed"],
        latest["aqi"],
        latest["pm25"]
    )

    st.metric(
        "Environmental Health Index",
        score
    )

    st.write(
        f"Status: {status}"
    )

    st.dataframe(df)

except Exception:
    st.warning("Collect data first")