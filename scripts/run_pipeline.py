#!/usr/bin/env python
# 여기에 obsidian_txtmining 모듈 조합 예제 pipeline 코드 작성
import sys, os

# Set matplotlib backend to Agg to prevent main thread errors in non-GUI env
import matplotlib
matplotlib.use('Agg')

# Add project root to sys.path to allow running as script without installation
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

# Import logic
try:
    from obsidian_txtmining.config import MERGED_OUTPUT_FILE, VAULT_PATH, CUSTOM_STOPWORDS, DESIRED_POS_TAGS, DOC_SEPARATOR, FONT_PATH, VECTOR_PATH, DOC_VECTOR_PATH, FEATURE_NAMES_PATH, TOKEN_PATH
    from obsidian_txtmining.file_collector import collect_md_files
    from obsidian_txtmining.md_preprocessor import preprocess_markdown
    from obsidian_txtmining.tokenizer import Tokenizer
    from obsidian_txtmining.vectorizer import DocumentVectorizer
    from obsidian_txtmining.visualizer import plot_top_words, plot_wordcloud
    from obsidian_txtmining.saver import save_vectorizer, save_matrix, save_features, save_token
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Please make sure you are in the project root or have installed the package.")
    sys.exit(1)

def main():
    if not VAULT_PATH:
        print("[ERROR] VAULT_PATH environment variable is not set.")
        print("Please set it pointing to your Obsidian vault.")
        print("Example (PowerShell): $env:VAULT_PATH='C:\\My\\Vault'")
        sys.exit(1)

    if not os.path.exists(VAULT_PATH):
        print(f"[ERROR] Vault path does not exist: {VAULT_PATH}")
        sys.exit(1)

    markdown_files = collect_md_files(VAULT_PATH)
    print(f"\nFound {len(markdown_files)} markdown files in '{VAULT_PATH}'.")

    if not markdown_files:
        print("No markdown files found. Exiting.")
        return

    preprocessed_contents = []
    for i, file_path in enumerate(markdown_files):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            preprocessed_content = preprocess_markdown(content)
            if preprocessed_content:
                preprocessed_contents.append(preprocessed_content)
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    # Concatenate all preprocessed contents with a document separator
    merged_text = DOC_SEPARATOR.join(preprocessed_contents)

    try:
        with open(MERGED_OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write(merged_text)
        print(f"\nSuccessfully merged {len(preprocessed_contents)} documents into '{MERGED_OUTPUT_FILE}'.")
    except Exception as e:
        print(f"Error writing merged text to {MERGED_OUTPUT_FILE}: {e}")

    # Tokenization (for Document Recommendation)
    print("\n[1/3] Processing Documents...")
    tokenizer = Tokenizer(stopwords=CUSTOM_STOPWORDS, pos_tags=DESIRED_POS_TAGS)
    
    # 1. Document Level Data
    doc_objs = []
    for i, content in enumerate(preprocessed_contents):
        doc_objs.append({
            'content': tokenizer.tokenize(content),
            'source': os.path.basename(markdown_files[i]),
            'original_text': content  # Keep original for display
        })
    tokenized_docs = [d['content'] for d in doc_objs]

    # 2. Paragraph Level Data
    print("[2/3] Processing Paragraphs...")
    para_objs = []
    for i, content in enumerate(preprocessed_contents):
        # Split by double newline (paragraphs)
        paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
        for para in paragraphs:
            para_tokens = tokenizer.tokenize(para)
            if len(para_tokens) > 1: # Ignore tiny paragraphs
                para_objs.append({
                    'content': para_tokens,
                    'source': os.path.basename(markdown_files[i]),
                    'original_text': para
                })
    tokenized_paras = [p['content'] for p in para_objs]

    # 3. Sentence Level Data
    print("[3/3] Processing Sentences...")
    sent_objs = []
    for i, content in enumerate(preprocessed_contents):
        # Simple splitting by sentence terminators
        # Note: Ideally use a robust sentence splitter like kss or nltk, but regex for now
        import re
        sentences = re.split(r'(?<=[.?!])\s+', content)
        for sent in sentences:
            sent = sent.strip()
            if not sent: continue
            sent_tokens = tokenizer.tokenize(sent)
            if len(sent_tokens) > 1:
                sent_objs.append({
                    'content': sent_tokens,
                    'source': os.path.basename(markdown_files[i]),
                    'original_text': sent
                })
    tokenized_sents = [s['content'] for s in sent_objs]


    # Vectorization
    print("\nBuilding TF-IDF Indices...")
    
    # Doc Level
    doc_vectorizer = DocumentVectorizer()
    doc_vectors = doc_vectorizer.fit_transform(tokenized_docs)
    print(f" - Document Index: {doc_vectors.shape[0]} docs, {doc_vectors.shape[1]} features")

    # Para Level
    from obsidian_txtmining.config import PARA_VECTORIZER_PATH, PARA_MATRIX_PATH, SENT_VECTORIZER_PATH, SENT_MATRIX_PATH
    para_vectorizer = DocumentVectorizer()
    para_vectors = para_vectorizer.fit_transform(tokenized_paras)
    print(f" - Paragraph Index: {para_vectors.shape[0]} paragraphs")

    # Sent Level
    sent_vectorizer = DocumentVectorizer()
    sent_vectors = sent_vectorizer.fit_transform(tokenized_sents)
    print(f" - Sentence Index: {sent_vectors.shape[0]} sentences")

    
    # Visualization (Merged)
    merged_tokens = " ".join(tokenized_docs)
    tokens_list = merged_tokens.split()
    if tokens_list:
        plot_top_words(tokens_list, font_path=FONT_PATH)
        plot_wordcloud(tokens_list, font_path=FONT_PATH)  
        save_token(tokens_list, TOKEN_PATH)
    else:
        print("No tokens found in merged text. Skipping visualization.")

    # Save All Models
    save_vectorizer(doc_vectorizer, VECTOR_PATH)
    save_matrix(doc_vectors, DOC_VECTOR_PATH)
    save_features(doc_vectorizer.get_feature_names(), FEATURE_NAMES_PATH)
    
    save_vectorizer(para_vectorizer, PARA_VECTORIZER_PATH)
    save_matrix(para_vectors, PARA_MATRIX_PATH)
    
    save_vectorizer(sent_vectorizer, SENT_VECTORIZER_PATH)
    save_matrix(sent_vectors, SENT_MATRIX_PATH)
    
    print("Pipeline finished successfully.")

    # Recommendation System loop
    from obsidian_txtmining.recommender import recommend_document
    print("\n=== Multi-Level Personal Recommender ===")
    print("Enter a query to find similar [Documents / Paragraphs / Sentences / Keywords].")
    
    while True:
        user_input = input("\nQuery (or 'exit'): ").strip()
        if user_input.lower() in ['exit', 'quit']:
            break
        
        try:
            results = recommend_document(
                user_input=user_input,
                tokenizer=tokenizer,
                doc_vectorizer=doc_vectorizer, doc_matrix=doc_vectors, doc_objs=doc_objs,
                para_vectorizer=para_vectorizer, para_matrix=para_vectors, para_objs=para_objs,
                sent_vectorizer=sent_vectorizer, sent_matrix=sent_vectors, sent_objs=sent_objs,
                top_n=3
            )
            
            if not results:
                print("Query processing failed (empty?).")
                continue
            
            # Display Results
            print(f"\n >>> Related Keywords: {', '.join(results['keywords'])}")
            
            print("\n [1] Top Documents:")
            if not results['documents']: print("    (No match)")
            for r in results['documents']:
                print(f"    - {r['source']} (Score: {r['score']:.2f})")
            
            print("\n [2] Top Paragraphs:")
            if not results['paragraphs']: print("    (No match)")
            for r in results['paragraphs']:
                text_preview = r['content'][:100] + "..." if len(r['content']) > 100 else r['content']
                print(f"    - \"{text_preview}\"")
                print(f"      Source: {r['source']} (Score: {r['score']:.2f})")

            print("\n [3] Top Sentences:")
            if not results['sentences']: print("    (No match)")
            for r in results['sentences']:
                print(f"    - \"{r['content']}\"")
                print(f"      Source: {r['source']} (Score: {r['score']:.2f})")

        except Exception as e:
            print(f"Error during recommendation: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    main()

