import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


def tfidf_search(question, tfidf_vectorizer, top_d=5):
    # lowercasing before encoding
    query_embedded = tfidf_vectorizer.transform([question.lower()])
    cosine_scores = cosine_similarity(query_embedded, context_embedded)[0]

    # Get top x cosinr score and index its
    results = []
    for idx in cosine_scores.argsort()[-top_d:][::-1]:
        doc_score = {
            'id': idx,
            'cosine_score': cosine_scores[idx]
        }
        results.append(doc_score)
    return results


if __name__ == '__main__':
    vi_data_df = pd.read_csv('vi_text_retrieval.csv')

    context = vi_data_df['text']
    context = [doc.lower() for doc in context]

    tfidf_vectorizer = TfidfVectorizer()
    context_embedded = tfidf_vectorizer.fit_transform(context)

    question = vi_data_df.iloc[0]['question']
    results = tfidf_search(question, tfidf_vectorizer)
    print(results[0]['cosine_score'])
