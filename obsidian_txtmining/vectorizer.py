from sklearn.feature_extraction.text import TfidfVectorizer

class DocumentVectorizer:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def fit_transform(self, docs):
        return self.vectorizer.fit_transform(docs)

    def transform(self, docs):
        return self.vectorizer.transform(docs)

    def get_feature_names(self):
        return self.vectorizer.get_feature_names_out()
