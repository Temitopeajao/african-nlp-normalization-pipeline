import pandas as pd
from tqdm import tqdm
from pipeline.normalizer import AfricanTextNormalizer
from pipeline.detector import LanguageDetector
from pipeline.validator import validate_diacritics_preserved


def process_dataset(input_path: str, output_path: str, language: str = "yoruba"):
    df = pd.read_csv(input_path)

    normalizer = AfricanTextNormalizer(language=language)
    detector = LanguageDetector()

    results = []

    for _, row in tqdm(df.iterrows(), total=len(df), desc="Normalizing"):
        raw_text = str(row["text"])

        clean_text = normalizer.normalize(raw_text)
        profile = detector.get_language_profile(clean_text)
        validation = validate_diacritics_preserved(raw_text, clean_text, language)

        results.append({
            "raw_text": raw_text,
            "clean_text": clean_text,
            "char_count_before": len(raw_text),
            "char_count_after": len(clean_text),
            "language_detected": profile["primary_language"],
            "is_code_switched": profile["is_code_switched"],
            "confidence": profile.get("primary_confidence", 0),
            "diacritics_preserved": validation["diacritics_preserved"]
        })

    output_df = pd.DataFrame(results)
    output_df.to_csv(output_path, index=False)

    print(f"\n✅ Processing complete")
    print(f"Total samples: {len(output_df)}")
    print(f"Code-switched samples: {output_df['is_code_switched'].sum()}")
    print(f"Avg chars removed: {(output_df['char_count_before'] - output_df['char_count_after']).mean():.1f}")
    print(f"Diacritics fully preserved: {output_df['diacritics_preserved'].sum()}/{len(output_df)}")


if __name__ == "__main__":
    process_dataset(
        input_path="data/raw/yoruba_corpus.csv",
        output_path="data/processed/yoruba_clean.csv",
        language="yoruba"
    )
