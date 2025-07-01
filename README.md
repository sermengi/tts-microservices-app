# Text-to-Speech Microservices Project

This project is a simple text-to-speech (TTS) application built using a microservice architecture. The primary goal is to demonstrate how to build, containerize, and orchestrate independent Python services.

## Architecture Overview

The application is composed of three distinct microservices:

* **Frontend Service:** A simple web interface built with Streamlit that allows users to input text.
* **API Gateway for Routing**: Routes requests to internal services
* **Text Preprocessing Service**: Cleans and normalizes user input text
* **TTS Model Inference Service**: Converts user input text to speech
* **Audio Service**: Serves and stored converted audio files


### Communication Flow

1.  A user submits text through the **Frontend Service**.
2.  The **Frontend Service** sends the text to the **API Gateway**.
3.  The **API Gateway** sends the text to the **Text Preprocessing Service** for preprocessing.
4.  The **Text Preprocessing Service** send the processed text to audio file to the **TTS Model Inference Service**.
5. The **TTS Model Inference Service** returns the generated audio file to the **Audio Service**.
6.  The **Audio Service** saves the audio and returns its location to the **Frontend Service**.
7.  The **Frontend Service** provides a link for the user to play or download the audio.

## Folder Structure
```bash
tts-microservices-app\
├── LICENSE
├── README.md
├── api-gateway
│   ├── Dockerfile
│   └── main.py
├── audio-service
│   ├── Dockerfile
│   └── main.py
├── docker-compose.yml
├── preprocessing-service
│   ├── Dockerfile
│   └── main.py
├── tts-service
│   ├── Dockerfile
│   └── main.py
└── web_ui
    └── app.py
```
