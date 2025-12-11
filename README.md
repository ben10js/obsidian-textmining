# Personal Knowledge Recommender System

## Overview
This project is a personalized recommendation engine designed to analyze a private Obsidian knowledge base (Markdown notes). Unlike generic search engines, it discovers latent semantic connections between notes by calculating similarity at multiple levels (Document, Paragraph, Sentence). It was developed to enhance metacognitive processes by surfacing relevant past thoughts and context during the writing process.
<img width="1000" height="500" alt="word_cloud" src="https://github.com/user-attachments/assets/f35e4458-f0de-4557-aaa6-308da0093eb6" />
<img width="1200" height="700" alt="frq_chart" src="https://github.com/user-attachments/assets/40440685-d0af-420f-a65a-700121c620eb" />

## Data
- **Source**: Personal Obsidian Vault (Markdown files).
- **Type**: Unstructured Korean/Mixed text data.
- **Preprocessing**: 
  - Extracted raw text from Markdown (removed YAML frontmatter, syntax, tables).
  - Cleaned noise (special characters, URLs).
  - Segmentation into Document, Paragraph (double newline), and Sentence (punctuation) units.

## Methods
- **NLP Preprocessing**: Morphological analysis using **KoNLPy (Okt)** and custom stopword filtering to handle Korean agglutinative traits.
- **Feature Extraction**: **TF-IDF (Term Frequency-Inverse Document Frequency)** vectorization to represent text and lower the weight of common but uninformative tokens.
- **Similarity Measure**: **Cosine Similarity** to calculate the distance between the user query and knowledge units in a high-dimensional vector space.
- **Hierarchical Indexing**: Built three separate vector indices (Document, Paragraph, Sentence) to provide multi-granular recommendations.

## Results
- **Multi-Level Retrieval**: Successfully implemented a 4-level search capability (Document, Paragraph, Sentence, and Related Keywords).
- **Semantics over Keywords**: Capable of finding semantically related notes even without exact keyword matching in the title, overcoming the limitations of standard file search.
- **Performance**: Achieved meaningful retrieval relevance (Similarity Score ~0.15–0.35) within a sparse, highly personalized small-data environment.

## How to run

### 1. Requirements
- Python 3.8+
- Java (JDK) for KoNLPy

### 2. Installation
```bash
git clone https://github.com/ben10js/obsidian-textmining.git
cd obsidian-textmining
pip install -r requirements.txt
```

### 3. Execution
Set your Obsidian Vault path containing Markdown notes:

**Windows (PowerShell)**:
```powershell
$env:VAULT_PATH = "C:\Path\To\Your\Vault"
python scripts/run_pipeline.py
```

**Linux/Mac**:
```bash
export VAULT_PATH="/path/to/your/vault"
python scripts/run_pipeline.py
```

## What I learned
- **Handling Sparsity**: Learned that in small, personal corpora, standard TF-IDF can suffer from sparsity; splitting data into smaller units (sentences/paragraphs) significantly improves context retrieval.
- **Text Preprocessing**: Gained experience in cleaning unstructured Markdown data and handling mixed-language (Korean/English) tokenization issues.
- **Pipeline Segregation**: Understood the importance of decoupling the indexing pipeline (Tokenizer -> Vectorizer) from the inference engine (Recommender) for modularity.
