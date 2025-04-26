import os
import json
from pypdf import PdfReader

def extract_text_from_pdfs(pdf_folder_path):
    pdf_data = {}
    
    # List all PDF files in the folder
    for filename in os.listdir(pdf_folder_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(pdf_folder_path, filename)
            try:
                reader = PdfReader(file_path)
                text = ""
                for page in reader.pages:
                    content = page.extract_text()
                    if content:
                        text += content + "\n"
                pdf_data[filename] = text.strip()
            except Exception as e:
                print(f"❌ Error reading {filename}: {e}")
                pdf_data[filename] = ""

    return pdf_data

def save_to_json(data, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\n✅ Extracted data saved to: {output_path}")

if __name__ == "__main__":
    # Path to the folder containing PDF files
    pdf_folder = "data"

    # Path to save JSON
    output_json = "extracted_text.json"

    # Extract and save
    extracted_texts = extract_text_from_pdfs(pdf_folder)
    save_to_json(extracted_texts, output_json)
