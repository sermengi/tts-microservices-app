import os

import requests
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI(
    title="Text-to-Speech API Gateway",
    description="API Gateway for TTS Microservice",
    version="1.0.0",
)

PREPROCESS_URL = os.getenv("PREPROCESS_URL", "http://localhost:8001/preprocess")
TTS_URL = os.getenv("TTS_URL", "http://localhost:8002/synthesize")


class TextInput(BaseModel):
    text: str


@app.post("/preprocess")
async def forward_to_preprocessing(input: TextInput):
    try:
        preprocessed_text = requests.post(
            f"{PREPROCESS_URL}", json=input.dict(), timeout=5
        )
        preprocessed_text.raise_for_status()
        return preprocessed_text.json()
    except requests.RequestException as e:
        return HTTPException(status_code=502, detail=str(e))


@app.post("/synthesize")
def synthesize_speech(input: TextInput):
    try:
        response = requests.post(PREPROCESS_URL, json=input.dict(), timeout=5)
        response.raise_for_status()
        preprocessed = response.json()
        normalized_text = preprocessed.get("normalized_text")
        if not normalized_text:
            raise ValueError("Preprocessing did not return normalized_text.")

        tts_response = requests.post(
            TTS_URL, json={"text": normalized_text}, timeout=15
        )
        tts_response.raise_for_status()

        with open("speech.wav", "wb") as f:
            f.write(tts_response.content)

        return FileResponse("speech.wav", media_type="audio/wav", filename="speech.wav")
    except (requests.RequestException, ValueError) as e:
        raise HTTPException(status_code=502, detail=f"TTS pipeline failed: {str(e)}")
