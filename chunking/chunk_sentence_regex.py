import json
import re

class SentenceChunkerRegex:
    def __init__(self, max_sentences=5):
        self.max_sentences = max_sentences

    def split_into_sentences(self, text):
        sentence_endings = re.compile(r'(?<=[.!?]) +')
        sentences = sentence_endings.split(text)
        return [s.strip() for s in sentences if s.strip()]

    def chunk(self, text):
        sentences = self.split_into_sentences(text)
        return [' '.join(sentences[i:i + self.max_sentences]) for i in range(0, len(sentences), self.max_sentences)]

    def process_and_save(self, input_file, output_file):
        try:
            with open(input_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            chunked_data = {}
            for doc, text in data.items():
                try:
                    chunked_data[doc] = self.chunk(text)
                except Exception as e:
                    print(f"❌ Error chunking '{doc}': {e}")
                    chunked_data[doc] = []

            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(chunked_data, f, indent=2)

            print(f"✅ Sentence-based (regex) chunking completed. Saved to {output_file}")
        except Exception as e:
            print(f"❌ Error during sentence-based chunking: {e}")

if __name__ == "__main__":
    chunker = SentenceChunkerRegex(max_sentences=5)
    chunker.process_and_save("../preprocessed_text.json", "chunks_sentence_regex.json")
