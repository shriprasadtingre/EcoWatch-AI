import streamlit as st
import pandas as pd

from chatbot.gemini_bot import (
    ask_environment_ai
)

st.header(
    "EcoWatch AI Assistant"
)

df = pd.read_csv(
    "data/raw/environment_data.csv"
)

latest = df.iloc[-1]

question = st.text_input(
    "Ask about environment"
)

if st.button(
    "Analyze"
):

    if question:

        with st.spinner(
            "Thinking..."
        ):

            result = ask_environment_ai(
                question,
                latest
            )

        st.write(
            result
        )