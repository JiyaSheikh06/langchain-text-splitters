from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Artificial Intelligence is a branch of computer science.
Machine Learning enables computers to learn patterns from data.
Deep Learning uses neural networks with multiple layers.
Natural Language Processing helps computers understand human language.
"""

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
)

chunks = text_splitter.split_text(text)

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}:")
    print(chunk)
    print("Length:", len(chunk))