import streamlit as st
import pandas as pd

from prediction.health_index import calculate_ehi
from prediction.hazard_predictor import (
    predict_heatwave,
    predict_pollution
)

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

    heatwave = predict_heatwave(
        latest["temperature"],
        latest["humidity"]
    )

    pollution = predict_pollution(
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

    st.subheader("Hazard Prediction")

    st.write(
        f"Heatwave Risk: {heatwave}"
    )

    st.write(
        f"Pollution Risk: {pollution}"
    )

    st.subheader("Collected Data")

    st.dataframe(df)

except Exception as e:

    st.warning(
        "Collect environmental data first"
    )