import os

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

AUDIO_DIR = "audios"

app.mount("/audios", StaticFiles(directory=AUDIO_DIR), name="audios")


@app.get("/")
def read_root():
    return {"message": "Audio Service is running"}


@app.get("/get-audio/{filename}")
def get_audio(filename: str):
    file_path = os.path.join(AUDIO_DIR, filename)
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=404, detail="Audio file not found.")
    return FileResponse(path=file_path, media_type="audio/mpeg", filename=filename)
