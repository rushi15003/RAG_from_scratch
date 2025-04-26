# cosine_sim.py
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class CosineSimilaritySearch:
    def __init__(self, embeddings, text_data):
        self.embeddings = embeddings
        self.text_data = text_data

    def search(self, query_vector, top_k=3):
        try:
            similarities = cosine_similarity([query_vector], self.embeddings)[0]
            top_indices = np.argsort(similarities)[::-1][:top_k]
            top_scores = similarities[top_indices]
            top_texts = [self.text_data[i] for i in top_indices]
            return top_indices, top_scores, top_texts
        except Exception as e:
            print(f"❌ Error during cosine similarity search: {e}")
            return [], [], []
