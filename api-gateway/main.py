from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Text-to-Speech API Gateway",
    description="API Gateway for TTS Microservice",
    version="1.0.0",
)


class TextInput(BaseModel):
    text: str


@app.post("/tts")
async def process_text(input: TextInput):
    original_text = input.text
    cleaned_text = original_text.strip()

    fake_audio_url = "http://audio-service/fake_audio_output.mp3"

    return {
        "message": "Text processed successfully",
        "cleaned_text": cleaned_text,
        "audio_url": fake_audio_url,
    }
