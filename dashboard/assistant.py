import streamlit as st
import pandas as pd

from chatbot.assistant import (
    environmental_chat
)

st.header(
    "AI Assistant"
)

df = pd.read_csv(
    "data/raw/environment_data.csv"
)

latest = df.iloc[-1]

question = st.text_input(
    "Ask"
)

if question:

    st.write(
        environmental_chat(
            question,
            latest
        )
    )