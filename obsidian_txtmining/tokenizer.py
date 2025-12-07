import re
from konlpy.tag import Okt
import spacy

class Tokenizer:
    def __init__(self, stopwords, pos_tags):
        self.okt = Okt()
        self.nlp = spacy.load('en_core_web_sm')   # 영어 모델 로드
        self.stopwords = set(stopwords)
        self.pos_tags = set(pos_tags)

    def is_korean(self, text):
        # 한글이 일정 비율 이상이면 한국어로 판단
        kor_ratio = len(re.findall(r'[가-힣]', text)) / (len(text)+1e-10)
        return kor_ratio > 0.1

    def tokenize_korean(self, text):
        preprocessed_tokens = []
        pos_tags_for_text = self.okt.pos(text, norm=True, stem=True)
        for morpheme, pos_tag in pos_tags_for_text:
            if pos_tag in self.pos_tags:
                morpheme_lower = morpheme.lower()
                if morpheme_lower not in self.stopwords:
                    cleaned_morpheme = re.sub(r'[^가-힣a-zA-Z]', '', morpheme_lower)
                    if len(cleaned_morpheme) >= 2:
                        preprocessed_tokens.append(cleaned_morpheme)
        return ' '.join(preprocessed_tokens)

    def tokenize_english(self, text):
        doc = self.nlp(text)
        tokens = [t.lemma_.lower() for t in doc if t.is_alpha and not t.is_stop]
        return ' '.join(tokens)

    def tokenize(self, text):
        # 자동 분기
        if self.is_korean(text):
            return self.tokenize_korean(text)
        else:
            return self.tokenize_english(text)
        
    def each_tokenize(self, doc_list):
        preprocessed_list_tokens = []
        for doc in doc_list:
            doc_tokens = []
            pos_tags_for_doc = self.okt.pos(doc, norm=True, stem=True)

            for morpheme, pos_tag in pos_tags_for_doc:
                if pos_tag in self.pos_tags:
                    morpheme_lower = morpheme.lower()
                    if morpheme_lower not in self.stopwords:
                        cleaned_token = re.sub(r'[^가-힣a-zA-Z]', '', morpheme_lower)
                        if len(cleaned_token) >= 2:
                            doc_tokens.append(cleaned_token)
            preprocessed_list_tokens.append(' '.join(doc_tokens))
        return preprocessed_list_tokens
