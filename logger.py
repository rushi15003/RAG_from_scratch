# logger.py
import logging
import os

# Create logs folder if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(name)s — %(message)s",
    handlers=[
        logging.FileHandler("logs/rag_pipeline.log"),
        logging.StreamHandler()  # also print to console
    ]
)

# Create a logger instance
logger = logging.getLogger("RAG")
