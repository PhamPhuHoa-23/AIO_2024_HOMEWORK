import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


def corr_search(question, tfidf_vectorizer, top_d=5):
    # lower casing before encoding
    query_embedded = tfidf_vectorizer.transform([question.lower()])
    corr_scores = np.corrcoef(query_embedded.toarray()[0], context_embedded.toarray())
    corr_scores = corr_scores[0][1:]

    results = []
    for idx in corr_scores.argsort()[-top_d:][::-1]:
        doc_score = {
            'id': idx,
            'corr_score': corr_scores[idx]
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
    results = corr_search(question, tfidf_vectorizer, top_d=5)
    print(results[1]['corr_score'])
