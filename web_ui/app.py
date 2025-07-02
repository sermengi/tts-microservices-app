import os

import requests
import streamlit as st

# Read API URL from environment variable (fallback to localhost)
API_GATEWAY_URL = os.getenv("API_GATEWAY_URL", "http://localhost:8000")

st.set_page_config(page_title="Text-to-Speech App", layout="centered")

st.markdown("""
# Text-to-Speech Microservice Demo

Welcome to the TTS demo app!
This application converts the input text into speech using a set of microservices:
- Preprocessing
- TTS (Text-to-Speech)
- Audio streaming

Please enter your text below and hit **Submit** to hear the audio output.
""")

user_input = st.text_area(
    "Enter your text here:",
    height=200,
    placeholder="Hello, world! This is a test of the text-to-speech system.",
)

if st.button("Submit"):
    if user_input.strip() == "":
        st.warning("Please enter some text before submitting.")
    else:
        st.info("Sending text to backend for processing...")

        try:
            response = requests.post(
                f"{API_GATEWAY_URL}/tts", json={"text": user_input}
            )
            if response.status_code == 200:
                data = response.json()
                st.success("Processing complete.")
                st.write(f"Cleaned Text: '{data['cleaned_text']}'")
                st.audio(data["audio_url"])
            else:
                st.error(f"API returned error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            st.error(f"Failed to connect to backend: {e}")
