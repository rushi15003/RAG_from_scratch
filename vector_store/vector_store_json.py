# vector_store_json.py

import json

class JSONVectorStore:
    def __init__(self, filepath):
        self.filepath = filepath
        self.store = {}

    def add(self, chunk_id, vector, chunk):
        try:
            self.store[chunk_id] = {"vector": vector, "chunk": chunk}
        except Exception as e:
            print(f"❌ Error adding chunk {chunk_id}: {e}")

    def save(self):
        try:
            with open(self.filepath, "w") as f:
                json.dump(self.store, f, indent=2)
            print(f"✅ Store saved to {self.filepath}")
        except Exception as e:
            print(f"❌ Error saving store to {self.filepath}: {e}")

    def load(self):
        try:
            with open(self.filepath, "r") as f:
                self.store = json.load(f)
            return self.store
        except Exception as e:
            print(f"❌ Error loading store from {self.filepath}: {e}")
            return {}

    def get(self, chunk_id):
        try:
            return self.store.get(chunk_id)
        except Exception as e:
            print(f"❌ Error retrieving chunk {chunk_id}: {e}")
            return None
