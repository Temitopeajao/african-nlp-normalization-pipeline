from config.language_config import PRESERVED_CHARS


def validate_diacritics_preserved(original: str, normalized: str, language: str) -> dict:
    preserved = PRESERVED_CHARS.get(language, set())

    original_special = set(c for c in original if c in preserved)
    normalized_special = set(c for c in normalized if c in preserved)

    lost_chars = original_special - normalized_special

    return {
        "diacritics_preserved": len(lost_chars) == 0,
        "lost_characters": list(lost_chars),
        "original_diacritic_count": sum(1 for c in original if c in preserved),
        "normalized_diacritic_count": sum(1 for c in normalized if c in preserved)
    }
