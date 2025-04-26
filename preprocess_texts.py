import json
import re
import os
import logging

# === Setup Logger ===
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("rag_pipeline.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def preprocess_text(text):
    try:
        text = text.lower()
        text = text.encode("ascii", "ignore").decode()
        text = re.sub(r'-\s+', '', text)
        text = text.replace('\n', ' ').replace('\r', ' ')
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'[^\w\s\.\?!]', '', text)
        text = re.sub(r'\b[a-z]{2,}(?: [a-z]{2,}){0,2}(?: et al)?\.?(?: \d{4}){1,3}\b', '', text)
        text = re.sub(r'\bdoi\s*\d{7,}\b', '', text)
        text = re.sub(r'doi\d+', '', text)
        return text.strip()
    except Exception as e:
        logger.exception(f"❌ Error while preprocessing text: {e}")
        return ""

input_path = "extracted_text.json"
output_path = "preprocessed_text.json"

if not os.path.exists(input_path):
    logger.error(f"❌ File not found: {input_path}")
    exit()

try:
    with open(input_path, "r", encoding="utf-8") as infile:
        raw_data = json.load(infile)
except Exception as e:
    logger.exception(f"❌ Failed to load input JSON: {e}")
    exit()

preprocessed_data = {}

for filename, raw_text in raw_data.items():
    try:
        logger.info(f"✅ Preprocessing {filename}...")
        clean_text = preprocess_text(raw_text)
        preprocessed_data[filename] = clean_text
    except Exception as e:
        logger.exception(f"❌ Error preprocessing {filename}: {e}")
        preprocessed_data[filename] = ""

try:
    with open(output_path, "w", encoding="utf-8") as outfile:
        json.dump(preprocessed_data, outfile, indent=2)
    logger.info(f"🎉 Preprocessing complete! Output saved to '{output_path}'")
except Exception as e:
    logger.exception(f"❌ Failed to save preprocessed JSON: {e}")
