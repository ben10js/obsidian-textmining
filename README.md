# Personal Knowledge Recommender System

## Overview
This project is a personalized recommendation engine designed to analyze a private Obsidian knowledge base (Markdown notes). Unlike generic search engines, it discovers latent semantic connections between notes by calculating similarity at multiple levels (Document, Paragraph, Sentence). It was developed to enhance metacognitive processes by surfacing relevant past thoughts and context during the writing process.
<img src="https://github.com/user-attachments/assets/f35e4458-f0de-4557-aaa6-308da0093eb6" alt="word_cloud" width="400" style="display:inline-block;"/>
<img src="https://github.com/user-attachments/assets/40440685-d0af-420f-a65a-700121c620eb" alt="frq_chart" width="400" style="display:inline-block;"/>
```
=== Multi-Level Personal Recommender ===
Enter a query to find similar [Documents / Paragraphs / Sentences / Keywords].

Query (or 'exit'): 반사이익에 대해 내가 생각한 것들이 뭐였지

 >>> Related Keywords: 평가자, 이익, 평가, 희소성, 상여

 [1] Top Documents:
    - 5.10 반사이익.md (Score: 0.28)
    - 5.6 우연하게 찾은 자기심리학.md (Score: 0.14)
    - 2024-08-20 자본주의에서 기회(금광)이 있는 곳.md (Score: 0.14)

 [2] Top Paragraphs:
    - "'반사이익'이라는 표현에 대해서 내가 군대 와서 함중사를 보고 얻은 여성을 대할 때의 차분함과 진중함. 병사들 사이에서 선행을 기꺼이 베풀고 계산하지 않고 짬인지 오버해서하는 등의..."
      Source: 5.10 반사이익.md (Score: 0.28)
    - "Obsidian에서 각 파일을 단순히 back link로 연결하는 것보다, 태그를 통해 먼저 범주를 만들어주는 것이 obsidian에서 내 생각들 사이의 체계를 형성하는 데에 훨씬..."
      Source: 5.6 우연하게 찾은 자기심리학.md (Score: 0.14)
    - "자본주의는 빈틈이 없다. 균형으로 이어진다. 효율이 안좋았다고 생각해도, 계산에 포함하는 기간을 늘리면 장기적으로는 균형으로 이어진다. 헬빨았다고 생각해도 꿀빨았던 적이 있었 기에 ..."
      Source: 2024-08-20 자본주의에서 기회(금광)이 있는 곳.md (Score: 0.14)

 [3] Top Sentences:
    - "두 곳이 있다고 생각한다."
      Source: 2024-08-20 자본주의에서 기회(금광)이 있는 곳.md (Score: 0.45)
    - "생각보다.."
      Source: 70.16 법이란 무엇인가.md (Score: 0.45)
    - "평화에서의 농업이익보다, 전쟁 후 침략이익이 더 컸다."
      Source: 10.12 자율신경 균형 검사.md (Score: 0.44)

Query (or 'exit'): 주관적

 >>> Related Keywords: 평가자, 이익, 평가, 희소성, 상여

 [1] Top Documents:
    - 5.10 반사이익.md (Score: 0.10)
    - 6.27 수학 과학 언어 역사, 그리고 예체능.md (Score: 0.06)
    - 추가데이터.md (Score: 0.04)

 [2] Top Paragraphs:
    - "'반사이익'이라는 표현에 대해서 내가 군대 와서 함중사를 보고 얻은 여성을 대할 때의 차분함과 진중함. 병사들 사이에서 선행을 기꺼이 베풀고 계산하지 않고 짬인지 오버해서하는 등의..."
      Source: 5.10 반사이익.md (Score: 0.10)
    - "쇼펜하우어 '여록과 보유/교육에 대하여' 부분 참고 아이는 판단을 할 수 없음. 그래서 직관을 개발하거나 경험을 하는 것이 좋다. 하지만 개념 또한 존재하며 이 개념을 가지고 하는..."
      Source: 6.27 수학 과학 언어 역사, 그리고 예체능.md (Score: 0.06)
    - "언어에 대한 고찰, 영어를 사용해서 수학을 공부하려고 노력해봤지만 쉽지 않았다. 한국어로 했을 때 이해의 깊이와 속도가 훨씬 빨랐다. 그러다 문득 이런 생각이 들었다. 영어를 하고..."
      Source: 추가데이터.md (Score: 0.04)

 [3] Top Sentences:
    - "가공된 것일수록 누군가의 주관이 더 많이 녹아있다."
      Source: 추가데이터.md (Score: 0.42)
    - "그것을 바라보는 시선(주관)에서도 나온다.== 여기서는 대상 그 자체에 대한 부분은 도외시하고, 반사이익에 초첨을 맞추어 그 시선(평가자의 주관)에 집중해보자."
      Source: 5.10 반사이익.md (Score: 0.41)
    - "(주관적 인식) 2단계 : 시점이 자신과 주변의 경계에 있다."
      Source: 10.16 건선.md (Score: 0.39)
```

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
