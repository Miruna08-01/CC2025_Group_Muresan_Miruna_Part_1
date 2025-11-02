import streamlit as st
import requests

st.title("Frontend Streamlit")

try:
    response = requests.get("http://127.0.0.1:8000/api/data")
    data = response.json()
    st.success(f"Mesaj de la backend: {data['message']}")
except Exception as e:
    st.error("Nu s-a putut conecta la backend")