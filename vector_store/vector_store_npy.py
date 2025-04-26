# vector_store_npy.py

import numpy as np
import json
import os

class NPYVectorStore:
    def __init__(self, vector_path, meta_path):
        self.vector_path = vector_path
        self.meta_path = meta_path
        self.vectors = []
        self.metadata = []

    def add(self, vector, chunk_id, chunk_text):
        try:
            self.vectors.append(vector)
            self.metadata.append({"id": chunk_id, "chunk": chunk_text})
        except Exception as e:
            print(f"❌ Error adding vector for chunk {chunk_id}: {e}")

    def save(self):
        try:
            np.save(self.vector_path, np.array(self.vectors))
            with open(self.meta_path, "w") as f:
                json.dump(self.metadata, f, indent=2)
            print(f"✅ Vectors saved to {self.vector_path} and metadata to {self.meta_path}")
        except Exception as e:
            print(f"❌ Error saving data: {e}")

    def load(self):
        try:
            vectors = np.load(self.vector_path)
            with open(self.meta_path, "r") as f:
                metadata = json.load(f)
            return vectors, metadata
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            return None, None
