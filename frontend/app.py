import streamlit as st
import requests
from datetime import datetime
import time

st.set_page_config(page_title="FastAPI + Streamlit Demo", page_icon="🦄", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #74ABE2, #5563DE);
        color: white;
        text-align: center;
        font-family: "Helvetica Neue", sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🦋 Frontend Streamlit")
st.write("Real-time connection with FastAPI backend 💫")

backend_url = "https://cc2025-api.azurewebsites.net/api/data"

placeholder = st.empty()

try:
    response = requests.get(backend_url)
    data = response.json()

    message = data.get("message", "No message received 😢")
    backend_time = data.get("current_time", "Unknown")

    st.success(f"📩 Message from backend: **{message}**")
    st.info(f"🕒 Backend time: {backend_time}")

    # Show local time updating in real-time
    st.markdown("### ⏰ Local time")
    while True:
        local_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        placeholder.markdown(f"<h2 style='color:#FFF;'>🕓 {local_time}</h2>", unsafe_allow_html=True)
        time.sleep(1)

except Exception as e:
    st.error(f"🚨 Could not connect to backend: {e}")
