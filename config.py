# =========================
# Device Configuration
# =========================
DEVICE = "cpu"   # Force CPU usage


# =========================
# ASR (Whisper)
# =========================
# Use small or base for CPU. Avoid large models.
ASR_MODEL = "base"   # Options: tiny, base, small


# =========================
# Translation Model
# =========================
# English → French
TRANSLATION_MODEL = "Helsinki-NLP/opus-mt-en-fr"


# =========================
# TTS Model (French)
# =========================
# Lightweight French TTS model
TTS_MODEL = "tts_models/fr/css10/vits"


# =========================
# Audio Configuration
# =========================
SAMPLE_RATE = 16000
CHUNK = 1024


# =========================
# Performance Tweaks
# =========================
# Reduce generation length for CPU performance
MAX_NEW_TOKENS = 128

# Disable half precision (important for CPU)
USE_FP16 = False
