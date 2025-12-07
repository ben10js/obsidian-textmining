from sklearn.metrics.pairwise import cosine_similarity
import re

def recommend_document(
    user_input,
    tokenizer,
    # Level 1: Doc
    doc_vectorizer, doc_matrix, doc_objs,
    # Level 2: Paragraph
    para_vectorizer, para_matrix, para_objs,
    # Level 3: Sentence
    sent_vectorizer, sent_matrix, sent_objs,
    top_n=3
):
    """
    Multi-level recommendation: Document, Paragraph, Sentence, and Keywords.
    """
    results = {}
    
    # Preprocess User Query
    preprocessed_query = tokenizer.tokenize(user_input)
    if not preprocessed_query.strip():
        return None

    # Helper function for similarity search
    def search_level(vectorizer, matrix, objects, label):
        query_vec = vectorizer.transform([preprocessed_query])
        sims = cosine_similarity(query_vec, matrix).flatten()
        top_indices = sims.argsort()[-top_n:][::-1]
        
        level_results = []
        for idx in top_indices:
            if sims[idx] > 0.0:  # Only relevant matches
                level_results.append({
                    'index': idx,
                    'score': sims[idx],
                    'content': objects[idx]['original_text'],  # Display the readable original text
                    'source': objects[idx]['source']
                })
        return level_results

    # 1. Document Search
    results['documents'] = search_level(doc_vectorizer, doc_matrix, doc_objs, "Document")

    # 2. Paragraph Search
    results['paragraphs'] = search_level(para_vectorizer, para_matrix, para_objs, "Paragraph")
    
    # 3. Sentence Search
    results['sentences'] = search_level(sent_vectorizer, sent_matrix, sent_objs, "Sentence")

    # 4. Keyword Suggestion (Terms with highest TF-IDF in the top matching document)
    keywords = []
    if results['documents']:
        top_doc_idx = results['documents'][0]['index']
        feature_names = doc_vectorizer.get_feature_names()
        # Get tfidf vector for the top doc
        top_doc_vec = doc_matrix[top_doc_idx]
        # Sort indices by score
        sorted_indices = top_doc_vec.toarray().flatten().argsort()[::-1]
        # Top 5 keywords
        for i in range(5):
            idx = sorted_indices[i]
            if top_doc_vec[0, idx] > 0:
                keywords.append(feature_names[idx])
    
    results['keywords'] = keywords
    
    return results
