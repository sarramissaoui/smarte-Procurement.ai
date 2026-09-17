import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

stop_words_en = set(stopwords.words('english'))
stop_words_fr = set(stopwords.words('french'))


stop_words = stop_words_en.union(stop_words_fr)

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zàâçéèêëîïôûùüÿñæœ\s]', '', text)
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text