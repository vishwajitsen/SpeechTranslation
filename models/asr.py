import whisper
from config import ASR_MODEL, DEVICE

class ASRModel:
    def __init__(self):
        self.model = whisper.load_model(ASR_MODEL, device=DEVICE)


    def transcribe(self, audio_path):
        result = self.model.transcribe(audio_path)
        return result["text"]
