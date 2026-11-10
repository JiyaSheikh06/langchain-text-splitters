from langchain_text_splitters import CharacterTextSplitter

text = """
Artificial Intelligence is a branch of computer science.
Machine Learning is a subset of Artificial Intelligence.
Deep Learning uses neural networks with multiple layers.
"""

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=100,
    chunk_overlap=0,
)

chunks = text_splitter.split_text(text)

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}:")
    print(chunk)
    print("Length:", len(chunk))