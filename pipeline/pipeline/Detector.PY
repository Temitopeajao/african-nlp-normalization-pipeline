from langdetect import detect, detect_langs
from config.language_config import CODESWITCHING_THRESHOLD


class LanguageDetector:
    def detect_primary(self, text: str) -> str:
        try:
            return detect(text)
        except Exception:
            return "unknown"

    def is_code_switched(self, text: str) -> bool:
        """
        Detect if text mixes languages.
        Code-switched text needs different handling than monolingual text.
        """
        try:
            langs = detect_langs(text)
            if len(langs) > 1:
                return langs[1].prob > CODESWITCHING_THRESHOLD
        except Exception:
            pass
        return False

    def get_language_profile(self, text: str) -> dict:
        try:
            langs = detect_langs(text)
            return {
                "primary_language": langs[0].lang,
                "primary_confidence": round(langs[0].prob, 3),
                "is_code_switched": self.is_code_switched(text),
                "detected_languages": [
                    {"lang": l.lang, "prob": round(l.prob, 3)} for l in langs
                ]
            }
        except Exception:
            return {"primary_language": "unknown", "error": "Detection failed"}
