from logger import logger  # 👈 import logger
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


class TfidfSimilaritySearch:
    def __init__(self, text_chunks):
        logger.info("Initializing TfidfSimilaritySearch...")
        try:
            self.text_chunks = text_chunks
            self.vectorizer = TfidfVectorizer()
            self.embeddings = self.vectorizer.fit_transform(text_chunks)
            logger.info("TF-IDF embeddings generated successfully.")
        except Exception as e:
            logger.error(f"❌ Error during TF-IDF initialization: {e}")
            self.text_chunks = []
            self.embeddings = None

    def search(self, query, top_k=3):
        try:
            logger.info(f"Running similarity search for query: {query}")
            query_vector = self.vectorizer.transform([query])
            similarities = cosine_similarity(query_vector, self.embeddings).flatten()
            top_indices = similarities.argsort()[::-1][:top_k]
            logger.info(f"Top {top_k} indices: {top_indices}")
            return [(self.text_chunks[i], similarities[i]) for i in top_indices]
        except Exception as e:
            logger.error(f"❌ Error during search: {e}")
            return []


class MainPipeline:
    def __init__(self, json_path):
        logger.info("Initializing MainPipeline...")
        try:
            self.text_chunks = self.load_chunks_from_json(json_path)
            if self.text_chunks:
                self.search_engine = TfidfSimilaritySearch(self.text_chunks)
            else:
                self.search_engine = None
                logger.warning("No text chunks available for search.")
        except Exception as e:
            logger.error(f"❌ Error initializing pipeline: {e}")
            self.search_engine = None

    def load_chunks_from_json(self, path):
        logger.info(f"Loading JSON vector store from: {path}")
        try:
            with open(path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            chunks = []
            for entry in data.values():
                if isinstance(entry['chunk'], list):
                    chunks.extend(entry['chunk'])
                else:
                    chunks.append(entry['chunk'])
            logger.info(f"Loaded {len(chunks)} text chunks.")
            return chunks
        except Exception as e:
            logger.error(f"❌ Failed to load chunks from JSON: {e}")
            return []

    def run_similarity_search(self, query, top_k=3):
        try:
            if not self.search_engine:
                logger.error("❌ Search engine is not initialized.")
                return

            results = self.search_engine.search(query, top_k=top_k)
            if results:
                print("\nTop Retrieved Chunks (TF-IDF Cosine Similarity):\n")
                for i, (chunk, score) in enumerate(results, 1):
                    print(f"Result {i}:")
                    print(f"Similarity Score: {score:.4f}")
                    print(f"Retrieved Text:\n{chunk}\n")
                logger.info(f"Displayed top {top_k} results for query.")
            else:
                logger.warning("No results found for the query.")
        except Exception as e:
            logger.error(f"❌ Error during similarity search execution: {e}")


if __name__ == "__main__":
    json_path = r"C:\Users\prana\OneDrive\Desktop\RAG_SCRATCH\vector_storage\store.json"
    
    try:
        pipeline = MainPipeline(json_path)
        query = input("Enter the query for similarity search: ")
        pipeline.run_similarity_search(query, top_k=3)
    except Exception as e:
        logger.error(f"❌ Failed in main execution: {e}")
