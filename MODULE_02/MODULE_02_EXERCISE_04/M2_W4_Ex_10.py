import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


if __name__ == '__main__':
    vi_data_df = pd.read_csv('vi_text_retrieval.csv')

    context = vi_data_df['text']
    context = [doc.lower() for doc in context]

    tfidf_vectorizer = TfidfVectorizer()
    context_embedded = tfidf_vectorizer.fit_transform(context)
    print(context_embedded.toarray()[7][0])