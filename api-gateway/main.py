import os

import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Text-to-Speech API Gateway",
    description="API Gateway for TTS Microservice",
    version="1.0.0",
)

PREPROCESS_URL = os.getenv("PREPROCESS_URL", "http://localhost:8001/preprocess")


class TextInput(BaseModel):
    text: str


@app.post("/preprocess")
async def forward_to_preprocessing(input: TextInput):
    original_text = input.text
    try:
        preprocessed_text = requests.post(
            "http://localhost:8001/preprocess", json={"text": original_text}, timeout=5
        )
        preprocessed_text.raise_for_status()
        return preprocessed_text.json()
    except requests.RequestException as e:
        return HTTPException(status_code=502, detail=str(e))


# @app.post("/tts")
# async def process_text(input: TextInput):
#     original_text = input.text
#     cleaned_text = original_text.strip()

#     fake_audio_url = "http://audio-service/fake_audio_output.mp3"

#     return {
#         "message": "Text processed successfully",
#         "cleaned_text": cleaned_text,
#         "audio_url": fake_audio_url,
#     }
