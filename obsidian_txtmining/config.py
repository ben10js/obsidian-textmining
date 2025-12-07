import os

# 1. 경로 관련: Obsidian 볼트·결과파일·데이터폴더
# 기본값은 None으로 설정하여 사용자가 환경변수를 설정하도록 유도하거나, 실행 시 에러를 통해 안내
VAULT_PATH = os.getenv('VAULT_PATH') 

# 데이터 출력 디렉토리 (없으면 생성)
DATA_DIR = os.getenv('DATA_DIR', './data')
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR, exist_ok=True)

MERGED_OUTPUT_FILE = os.path.join(DATA_DIR, 'merged_obsidian_notes.txt')
WORDCLOUD_IMG_PATH = os.path.join(DATA_DIR, 'wordcloud.png')
PLOTS_PATH = os.path.join(DATA_DIR, 'plots')
if not os.path.exists(PLOTS_PATH):
    os.makedirs(PLOTS_PATH, exist_ok=True)

VECTOR_PATH = os.path.join(DATA_DIR, 'vectorizer_doc.joblib')
DOC_VECTOR_PATH = os.path.join(DATA_DIR, 'document_vectors.joblib')

PARA_VECTORIZER_PATH = os.path.join(DATA_DIR, 'vectorizer_para.joblib')
PARA_MATRIX_PATH = os.path.join(DATA_DIR, 'paragraph_vectors.joblib')

SENT_VECTORIZER_PATH = os.path.join(DATA_DIR, 'vectorizer_sent.joblib')
SENT_MATRIX_PATH = os.path.join(DATA_DIR, 'sentence_vectors.joblib')

FEATURE_NAMES_PATH = os.path.join(DATA_DIR, 'feature_names.joblib')
TOKEN_PATH = os.path.join(DATA_DIR, 'token.txt')

# 2. 불용어·품사 등 처리 파라미터
CUSTOM_STOPWORDS = [
    '이다', '있다', '하다', '되다', '것', '이', '그', '저', '수', '때', '말',
    '밖', '개', '원', '점', '요', '음', '씨', '분', '곳', '알', '나', '내', '들',
    '좀', '더', '줄', '게', '듯', '뿐', '채', '안', '영', '고', '면', '로', '에', '와',
    '과', '을', '를', '은', '는', '도', '만', '가', '의', '며', '서', '구', '하',
    '고', '받', '주', '아', '보', '같', '에서', '으로', '에게', '부터', '까지', 
    '으로서', '처럼', '만큼', '이라도', '라도', '마저', '조차', '커녕', '거나', 
    '든지', '다', '자', '니까', '습니다', 'ㅂ니다', '까', 'ㄹ까요', 'ㅂ시다', '읍시다', 
    '아요', '어요', '오', '이요', '세요', '시오'
]

DESIRED_POS_TAGS = ['Noun', 'Verb', 'Adjective', 'Adverb']
DOC_SEPARATOR = '\n=====\n'  # MD 파일 합치기 시 문서 구분자

# 3. 시각화용 한글폰트 등 환경 옵션
# Win: malgun.ttf / Mac: AppleGothic / Ubuntu/WSL: NanumGothic 등
FONT_PATH = os.getenv('FONT_PATH', "C:/Windows/Fonts/malgun.ttf")
WORDCLOUD_BACKGROUND = 'white'
RECOMMENDER_TOP_N = 3

# 4. 기타
DEBUG_MODE = os.getenv('DEBUG_MODE', 'False').lower() == 'true'
