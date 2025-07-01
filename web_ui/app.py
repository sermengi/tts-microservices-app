import streamlit as st

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
        # Placeholder for future API integration
        # audio_response = requests.post("http://api-gateway/tts", json={"text": user_input})
        st.success("Processing complete. (This is a placeholder.)")
