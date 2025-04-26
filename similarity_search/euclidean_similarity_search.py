# euclidean_similarity_search.py
import numpy as np

class EuclideanSimilaritySearch:
    def compute_similarity(self, query_vector, vectors):
        try:
            distances = []
            for vec in vectors:
                dist = np.linalg.norm(query_vector - vec)
                distances.append(dist)
            return distances
        except Exception as e:
            print(f"❌ Error computing Euclidean distances: {e}")
            return []
