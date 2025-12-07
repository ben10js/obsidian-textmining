
# Personal Recommender (Obsidian Text Mining)

A toolkit for analyzing an Obsidian Knowledge Base (Vault) using Korean text mining techniques (KonlPy, Scikit-learn).
It performs tokenization, vectorization (TF-IDF/Count), word cloud generation, and document recommendation based on similarity.

## Features
- **Markdown Processing**: Extracts text from Obsidian Markdown notes.
- **Korean Tokenization**: Uses `KonlPy` (Okt/Mecab) for morphological analysis.
- **Vectorization**: Creates document vectors for similarity search.
- **Visualization**: Generates word clouds and frequency plots.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ben10js/personal-recommender.git
   cd personal-recommender
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```
   *Note: Java (JDK) is required for KonlPy/JPype.*

## Usage

This project relies on environment variables for configuration to keep your data paths private.

1. **Set the Vault Path**:
   
   **PowerShell**:
   ```powershell
   $env:VAULT_PATH = "C:\Path\To\Your\Obsidian\Vault"
   python scripts/run_pipeline.py
   ```

   **Bash**:
   ```bash
   export VAULT_PATH="/path/to/your/vault"
   python scripts/run_pipeline.py
   ```

2. **(Optional) Custom Font**:
   If the WordCloud Korean font is broken, set `FONT_PATH`:
   ```bash
   export FONT_PATH="/path/to/malgun.ttf"
   ```

## Output
Results are saved in the `data/` directory:
- `wordcloud.png`: Word cloud image.
- `merged_obsidian_notes.txt`: Consolidated text.
- `*.joblib`: Serialized vectorizers and matrices.

## License
MIT
