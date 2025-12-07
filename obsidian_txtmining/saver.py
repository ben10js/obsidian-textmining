import joblib

def save_vectorizer(vectorizer, filepath):
    """
    vectorizer: scikit-learn TfidfVectorizer 객체 또는 커스텀 Wrapper
    filepath: 저장할 경로(예: 'vectorizer.joblib')
    """
    joblib.dump(vectorizer, filepath)

def load_vectorizer(filepath):
    """
    filepath: 저장된 벡터라이저 경로
    return: 불러온 vectorizer 객체
    """
    return joblib.load(filepath)

def save_matrix(matrix, filepath):
    joblib.dump(matrix, filepath)

def load_matrix(filepath):
    return joblib.load(filepath)

def save_features(feature_names, filepath):
    joblib.dump(feature_names, filepath)

def load_features(filepath):
    return joblib.load(filepath)

def save_token(token, filepath):
    joblib.dump(token, filepath)

def load_token(filepath):
    return joblib.load(filepath)