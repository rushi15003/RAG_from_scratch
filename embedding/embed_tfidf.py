import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

class TFIDFEmbedder:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def embed(self, chunks):
        return self.vectorizer.fit_transform(chunks)

    def process_and_save(self, input_file, vec_file, vocab_file):
        try:
            with open(input_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"❌ Error reading {input_file}: {e}")
            return

        try:
            all_chunks = []
            self.doc_map = []
            for doc, chunks in data.items():
                all_chunks.extend(chunks)
                self.doc_map.extend([(doc, i) for i in range(len(chunks))])

            matrix = self.embed(all_chunks)

            with open(vec_file, "wb") as f:
                np.save(f, matrix.toarray())

            with open(vocab_file, "wb") as f:
                pickle.dump(self.vectorizer, f)

            print(f"✅ TF-IDF embeddings saved to {vec_file}")
            print(f"✅ Vectorizer saved to {vocab_file}")
        except Exception as e:
            print(f"❌ Error during embedding or saving: {e}")

if __name__ == "__main__":
    embedder = TFIDFEmbedder()
    embedder.process_and_save(
        r"C:\Users\prana\OneDrive\Desktop\RAG_SCRATCH\chunking\chunks_sentence_regex.json",
        "embeddings_tfidf.npy",
        "tfidf_vectorizer.pkl"
    )
