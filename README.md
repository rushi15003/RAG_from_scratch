# RAG (Retrieval-Augmented Generation) Pipeline from Scratch

## 📁 Project Overview
This project demonstrates a **basic Retrieval-Augmented Generation (RAG)** pipeline built from scratch without using heavy libraries. It focuses on processing PDF documents, extracting text, chunking data, building vector stores, and performing semantic similarity search based on TF-IDF embeddings.

---

## 📊 Features
- **PDF Text Extraction**: Extracts text from PDF files.
- **Data Storage**: Saves extracted text into a structured JSON file.
- **TF-IDF Embeddings**: Converts text chunks into TF-IDF vectors.
- **Similarity Search**: Performs semantic search using cosine similarity.
- **Error Handling**: Proper try-except blocks for robust execution.
- **Logging**: Logs all important operations and errors for easier debugging.

---

## 💡 How It Works

1. **Extract Text from PDFs**:
   - Reads all PDF files inside the `data/` directory.
   - Extracts text page by page.
   - Saves extracted texts into `extracted_text.json`.

2. **TF-IDF Vectorization**:
   - Splits extracted texts into manageable chunks.
   - Creates TF-IDF embeddings of these chunks.

3. **Semantic Search**:
   - Accepts a user query from input.
   - Converts query into a TF-IDF vector.
   - Computes cosine similarity between query vector and text chunks.
   - Displays top-k most similar chunks.

4. **Multiple Distance Measures (optional)**:
   - Files like `cosine_sim.py`, `euclidean.py`, and `manhattan.py` allow different similarity calculations if needed.

---

## 🌟 Highlights
- Completely modular code.
- Easy to swap different similarity metrics.
- Well-structured error handling and logging.
- Minimalistic and beginner-friendly design.

---

## 🚀 Acknowledgements
- Inspired by real-world RAG pipelines.
- Built for educational and project portfolio purposes.

