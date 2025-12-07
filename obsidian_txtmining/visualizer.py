import collections
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def plot_top_words(tokens, font_path=None):
    word_counts = collections.Counter(tokens)
    df = pd.DataFrame(word_counts.most_common(), columns=['word', 'frequency'])
    plt.figure(figsize=(12, 7))
    # 폰트 지정(윈도우·맥·리눅스 환경별로)
    if font_path:
        import matplotlib.font_manager as fm
        plt.rc('font', family=fm.FontProperties(fname=font_path).get_name())
    else:
        plt.rc('font', family='Malgun Gothic')
    plt.bar(df['word'][:15], df['frequency'][:15])
    plt.xticks(rotation=45)
    plt.xlabel('Word')
    plt.ylabel('Frequency')
    plt.title('Top 15 Most Frequent Words')
    plt.tight_layout()
    plt.show()

def plot_wordcloud(tokens, font_path=None):
    wc = WordCloud(font_path=font_path, width=800, height=400, background_color='white').generate(' '.join(tokens))
    plt.figure(figsize=(10,5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud of Preprocessed Text')
    plt.show()
