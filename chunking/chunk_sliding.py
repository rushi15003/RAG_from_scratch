import json

class SlidingWindowChunker:
    def __init__(self, window_size=100, overlap=20):
        self.window_size = window_size
        self.overlap = overlap

    def chunk(self, text):
        words = text.split()
        step = self.window_size - self.overlap
        return [' '.join(words[i:i + self.window_size]) for i in range(0, len(words), step)]

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

            print(f"✅ Sliding window chunking completed. Saved to {output_file}")
        except Exception as e:
            print(f"❌ Error during sliding window chunking: {e}")

if __name__ == "__main__":
    chunker = SlidingWindowChunker(window_size=100, overlap=20)
    chunker.process_and_save("../preprocessed_text.json", "chunks_sliding.json")
