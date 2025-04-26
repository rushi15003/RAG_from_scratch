# vector_store_dict.py

class DictVectorStore:
    def __init__(self):
        self.store = {}  # {chunk_id: (vector, chunk)}

    def add(self, chunk_id, vector, chunk):
        try:
            self.store[chunk_id] = (vector, chunk)
        except Exception as e:
            print(f"❌ Error adding chunk {chunk_id}: {e}")

    def get(self, chunk_id):
        try:
            return self.store.get(chunk_id)
        except Exception as e:
            print(f"❌ Error retrieving chunk {chunk_id}: {e}")
            return None

    def get_all(self):
        try:
            return self.store
        except Exception as e:
            print(f"❌ Error retrieving all data: {e}")
            return {}
