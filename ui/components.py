import streamlit as st

def urgency_badge(level):
    colors = {
        "high": "red",
        "medium": "orange",
        "low": "green"
    }

    color = colors.get(level.lower(), "gray")

    st.markdown(
        f"""
        <div style="
            background-color:{color};
            padding:8px;
            border-radius:8px;
            color:white;
            width:120px;
            text-align:center;
            font-weight:bold;">
            {level.upper()}
        </div>
        """,
        unsafe_allow_html=True
    )