from app.tts_engine import synthesize_speech
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI(title="TTS Service")


class TextInput(BaseModel):
    text: str


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/synthesize")
def synthesize(input: TextInput):
    if not input.text.strip():
        raise HTTPException(status_code=400, detail="Text is empty.")
    try:
        audio_path = synthesize_speech(input.text)
        return FileResponse(audio_path, media_type="audio/wav", filename="speech.wav")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
