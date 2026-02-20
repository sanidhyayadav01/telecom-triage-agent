import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from agents.triage_agent import TelecomTriageAgent
from ui.components import urgency_badge

st.set_page_config(
    page_title="Telecom Triage Agent",
    page_icon="📡",
    layout="wide"
)

agent = TelecomTriageAgent()

st.title("📡 Telecom Support Triage Dashboard")

st.markdown(
"""
AI-powered telecom support automation system.
Classifies customer issues, extracts entities, and generates draft responses.
"""
)

message = st.text_area(
    "Customer Message",
    height=150,
    placeholder="Example: My internet has not been working since morning..."
)

if st.button("🚀 Analyze Ticket"):

    if message.strip():

        with st.spinner("Processing telecom request..."):
            result = agent.process(message)

        classification = result["classification"]

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📊 Urgency")
            urgency_badge(classification["urgency"])

        with col2:
            st.subheader("🧭 Intent")
            st.info(classification["intent"])

        st.subheader("📍 Routed To")
        st.success(result["route"])

        st.subheader("🧠 Extracted Entities")
        st.json(result["entities"])

        st.subheader("✉️ Draft Response")
        st.write(result["draft_response"])

    else:
        st.warning("Please enter a customer message.")