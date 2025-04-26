import json

class FixedSizeChunker:
    def __init__(self, chunk_size=100):
        self.chunk_size = chunk_size

    def chunk(self, text):
        words = text.split()
        return [' '.join(words[i:i + self.chunk_size]) for i in range(0, len(words), self.chunk_size)]

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

            print(f"✅ Fixed-size chunking completed. Saved to {output_file}")
        except Exception as e:
            print(f"❌ Error during fixed-size chunking: {e}")

if __name__ == "__main__":
    chunker = FixedSizeChunker(chunk_size=100)
    chunker.process_and_save("../preprocessed_text.json", "chunks_fixed.json")
