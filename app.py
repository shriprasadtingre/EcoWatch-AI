import streamlit as st

st.set_page_config(
    page_title="EcoWatch AI",
    layout="wide"
)

st.title(
    "EcoWatch AI"
)

page = st.sidebar.selectbox(
    "Navigate",
    [
        "Dashboard",
        "Forecast",
        "Assistant"
    ]
)

if page == "Dashboard":

    exec(
        open(
            "dashboard/home.py"
        ).read()
    )

elif page == "Forecast":

    exec(
        open(
            "dashboard/forecast.py"
        ).read()
    )

elif page == "Assistant":

    exec(
        open(
            "dashboard/assistant.py"
        ).read()
    )