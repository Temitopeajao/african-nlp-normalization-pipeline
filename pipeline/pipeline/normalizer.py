import unicodedata
import re
import ftfy
from config.language_config import PRESERVED_CHARS, OCR_ARTIFACTS


class AfricanTextNormalizer:
    def __init__(self, language: str = "yoruba"):
        self.language = language.lower()
        self.preserved = PRESERVED_CHARS.get(self.language, set())

    def fix_unicode(self, text: str) -> str:
        """Fix broken Unicode encoding — common in scraped web data"""
        return ftfy.fix_text(text)

    def normalize_composed_chars(self, text: str) -> str:
        """
        Normalize to NFC (composed form) — NOT NFKD.
        NFC preserves diacritics as single characters.
        NFKD would decompose them into base + combining marks,
        making them vulnerable to stripping.
        """
        return unicodedata.normalize('NFC', text)

    def fix_ocr_artifacts(self, text: str) -> str:
        """Repair common OCR errors in scanned documents"""
        for split, composed in OCR_ARTIFACTS["diacritic_split"].items():
            text = text.replace(split, composed)
        return text

    def remove_noise(self, text: str) -> str:
        """Remove noise while preserving linguistic content"""
        text = re.sub(r'http\S+|www\S+', '', text)
        text = re.sub(r'[!?]{2,}', '!', text)
        text = re.sub(r'\.{3,}', '...', text)
        text = re.sub(r'[^\w\s\'\-.,!?;:\u0080-\uFFFF]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    def normalize(self, text: str) -> str:
        """Full normalization pipeline"""
        text = self.fix_unicode(text)
        text = self.fix_ocr_artifacts(text)
        text = self.normalize_composed_chars(text)
        text = self.remove_noise(text)
        return text
