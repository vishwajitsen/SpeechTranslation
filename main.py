import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))




from audio.recorder import record_audio
from models.asr import ASRModel
from models.translator import Translator
from models.tts import SpeechSynthesizer
from utils.text_cleaner import clean_text


def main():
    audio_file = record_audio()

    asr = ASRModel()
    translator = Translator()
    tts = SpeechSynthesizer()

    print("🧠 Transcribing...")
    english_text = asr.transcribe(audio_file)
    english_text = clean_text(english_text)

    print("English:", english_text)

    print("🌍 Translating...")
    french_text = translator.translate(english_text)

    print("French:", french_text)

    tts.speak(french_text)


if __name__ == "__main__":
    main()
