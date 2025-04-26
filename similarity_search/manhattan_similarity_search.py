# manhattan_similarity_search.py
import numpy as np

class ManhattanSimilaritySearch:
    def compute_similarity(self, query_vector, vectors):
        try:
            distances = [np.sum(np.abs(query_vector - vec)) for vec in vectors]
            return distances
        except Exception as e:
            print(f"❌ Error computing Manhattan distances: {e}")
            return []
