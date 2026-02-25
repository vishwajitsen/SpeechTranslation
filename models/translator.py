from transformers import MarianMTModel, MarianTokenizer
from config import TRANSLATION_MODEL, DEVICE

class Translator:
    def __init__(self):
        self.tokenizer = MarianTokenizer.from_pretrained(TRANSLATION_MODEL)
        self.model = MarianMTModel.from_pretrained(TRANSLATION_MODEL).to(DEVICE)

    def translate(self, text):
        tokens = self.tokenizer(text, return_tensors="pt", padding=True).to(DEVICE)
        translated = self.model.generate(**tokens)
        output = self.tokenizer.decode(translated[0], skip_special_tokens=True)
        return output
