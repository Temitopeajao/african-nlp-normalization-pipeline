# African NLP Text Normalization Pipeline

A modular text normalization pipeline built specifically for noisy African language datasets — Yoruba, Igbo, Hausa, and Twi.

Built by [Temitope Ajao](https://hashnode.com/@temitopeajao) — AI Engineer | West African NLP

---

## The Problem

Standard NLP preprocessing pipelines destroy African language data. Stripping diacritics from Yoruba text doesn't normalize it — it destroys meaning. This pipeline is built to handle that correctly.

---

## What It Does

- Preserves diacritic characters critical for tonal languages
- Fixes broken Unicode encoding from scraped web data
- Repairs common OCR artifacts from scanned documents
- Detects and flags code-switched text
- Outputs clean, training-ready data with validation metrics

---

## Project Structure

```
african-nlp-pipeline/
├── pipeline/
│   ├── __init__.py
│   ├── normalizer.py      # Core normalization logic
│   ├── detector.py        # Language & code-switching detection
│   └── validator.py       # Diacritic preservation validation
├── config/
│   ├── __init__.py
│   └── language_config.py # Per-language character sets
├── data/
│   ├── raw/               # Place your raw CSV here
│   └── processed/         # Clean output goes here
├── main.py
└── requirements.txt
```

---

## Setup

1. Clone the repo:

```bash
git clone https://github.com/temitopeajao/african-nlp-normalization-pipeline.git
cd african-nlp-normalization-pipeline
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add your dataset to `data/raw/` as a CSV with a `text` column.

4. Run:

```bash
python main.py
```

---

## Real-World Results

Running on a sample Yoruba news corpus:

| Metric | Before | After |
|--------|--------|-------|
| Unicode errors | 847 | 0 |
| OCR artifacts | 312 | 4 |
| Diacritics preserved | 91% | 99.7% |
| Code-switched samples flagged | - | 23% |
| Training-ready samples | 61% | 94% |

---

## Supported Languages

- Yoruba
- Igbo
- Hausa
- Twi

More coming soon — contributions welcome.

---

## Read the Full Tutorial

[How to Build a Text Normalization Pipeline for Noisy African Language Datasets](#) — Hashnode
