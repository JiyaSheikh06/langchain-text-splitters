from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
    Language
)

text = """
def greet(name):
    print(f"Hello, {name}!")

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

class Calculator:
    def subtract(self, a, b):
        return a - b
"""

text_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=100,
    chunk_overlap=0,
)

chunks = text_splitter.split_text(text)

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}:")
    print(chunk)
    print("Length:", len(chunk))