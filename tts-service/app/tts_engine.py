import tempfile

from TTS.api import TTS

tts_model = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)


def synthesize_speech(text: str) -> str:
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as fp:
        output_path = fp.name
    tts_model.tts_to_file(text=text, file_path=output_path)
    return output_path


if __name__ == "__main__":
    text = "This is a test"
    output_path = synthesize_speech(text)
    print(output_path)
