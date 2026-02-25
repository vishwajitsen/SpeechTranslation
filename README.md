🎙️ Speech-to-Speech Translation System (S2ST)

A complete local Speech → Translation → Speech pipeline built using:

🎤 Whisper (ASR) – Speech-to-Text

🌍 Helsinki MarianMT (HuggingFace) – Translation

🗣️ Edge-TTS – Text-to-Speech

🔊 FFmpeg – Audio processing

The system records English speech from your microphone, translates it to French, and plays the translated speech automatically.

🚀 Architecture Overview
User Speech (Mic)
        ↓
Whisper ASR (Speech → English Text)
        ↓
MarianMT (English → French)
        ↓
Edge-TTS (French Text → French Audio)
        ↓
Auto Playback
📂 Project Structure
s2st_local/
│
├── main.py
├── models/
│   ├── asr.py
│   ├── translator.py
│   └── tts.py
│
├── myenv/ (virtual environment)
└── README.md


🛠 System Requirements

Windows 10 / 11

Python 3.12

FFmpeg installed and added to PATH

Internet connection (for first-time model download)

📦 Dependencies

Installed via pip:

openai-whisper

torch

transformers

sentencepiece

edge-tts

sacremoses

sounddevice (if recording locally)

numpy

🔧 Setup Instructions
1️⃣ Clone or Download Project

Place the project in:

C:\Speech_Translation\s2st_local
2️⃣ Create Virtual Environment
cd C:\Speech_Translation\s2st_local
python -m venv myenv

Activate:

myenv\Scripts\activate
3️⃣ Upgrade pip
python -m pip install --upgrade pip
4️⃣ Install Dependencies
pip install openai-whisper
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install transformers
pip install sentencepiece
pip install sacremoses
pip install edge-tts
pip install sounddevice numpy
5️⃣ Install FFmpeg (Required)
Download:

https://www.gyan.dev/ffmpeg/builds/

Extract to:

C:\ffmpeg

Add to PATH:

C:\ffmpeg

Verify:

ffmpeg -version

If version prints → installation successful.

▶️ How to Run

Activate environment:

cd C:\Speech_Translation\s2st_local
myenv\Scripts\activate

Run:

python main.py
🎯 Expected Output
🎙️ Speak now...
🛑 Recording finished
🧠 Transcribing...
English: Hello, how are you?
🌍 Translating...
French: Bonjour, comment allez-vous ?
🔊 Playing translated speech...

System will automatically generate and play French speech audio.

⚙️ Configuration
Change Target Language

Modify translator.py model:

Example:

TRANSLATION_MODEL = "Helsinki-NLP/opus-mt-en-de"

Available language models:
https://huggingface.co/Helsinki-NLP

Change TTS Voice

Modify inside tts.py:

SpeechSynthesizer(voice="fr-FR-DeniseNeural")

Available voices:
https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support

⚠️ Known Notes

First run downloads models (~300MB)

CPU-only setup (no GPU required)

FP16 warning is normal on CPU

HuggingFace symlink warning on Windows can be ignored



📌 Summary

This project demonstrates:

✔ End-to-end Speech Translation
✔ Fully Local Execution
✔ No cloud dependency
✔ Modular Architecture
✔ Production-ready structure# SpeechTranslation