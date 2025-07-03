from fastapi import FastAPI, HTTPException
from preprocess import preprocess_text
from pydantic import BaseModel

app = FastAPI(
    title="TTS Preprocessing Service",
    description="Microservice that cleans, normalizes, and segments text before TTS synthesis.",
    version="1.0.0",
)


class TextInput(BaseModel):
    text: str


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/preprocess")
def preprocess_endpoint(input: TextInput):
    if not input.text.strip():
        raise HTTPException(status_code=400, detail="Input text must not be empty.")

    try:
        result = preprocess_text(input.text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Preprocessing failed: {str(e)}")
