import asyncio
import edge_tts
import os

class SpeechSynthesizer:
    def __init__(self, voice="fr-FR-DeniseNeural"):
        self.voice = voice

    async def _speak_async(self, text, output_file):
        communicate = edge_tts.Communicate(text, self.voice)
        await communicate.save(output_file)

    def speak(self, text, output_file="output.mp3"):
        asyncio.run(self._speak_async(text, output_file))

        # 🔊 Play automatically (Windows)
        os.system(f"start {output_file}")