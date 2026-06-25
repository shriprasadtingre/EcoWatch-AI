import streamlit as st
import pandas as pd

from prediction.health_index import calculate_ehi
from prediction.hazard_predictor import (
    predict_heatwave,
    predict_pollution
)

from prediction.forecast import (
    forecast_next_days
)

from chatbot.assistant import (
    environmental_chat
)

st.title("EcoWatch AI")

try:

    df = pd.read_csv(
        "data/raw/environment_data.csv"
    )

    scores = []

    for _, row in df.iterrows():

        score, _ = calculate_ehi(
            row["temperature"],
            row["humidity"],
            row["wind_speed"],
            row["aqi"],
            row["pm25"]
        )

        scores.append(score)

    df["ehi"] = scores

    latest = df.iloc[-1]

    score = latest["ehi"]

    _, status = calculate_ehi(
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

    st.subheader(
        "Hazard Prediction"
    )

    st.write(
        f"Heatwave Risk: {heatwave}"
    )

    st.write(
        f"Pollution Risk: {pollution}"
    )

    st.subheader(
        "Future EHI Forecast"
    )

    forecast = forecast_next_days(
        df,
        "ehi",
        7
    )

    if forecast is not None:

        st.line_chart(
            forecast.set_index(
                "Day"
            )
        )

        st.dataframe(
            forecast
        )

    st.subheader(
        "AI Environmental Assistant"
    )

    question = st.text_input(
        "Ask about environment"
    )

    if question:

        reply = environmental_chat(
            question,
            latest
        )

        st.write(reply)

    st.subheader(
        "Collected Data"
    )

    st.dataframe(df)

except Exception as e:

    st.error(
        f"Error: {e}"
    )