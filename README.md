# LangChain Text Splitters

This repository contains practical examples of different text-splitting techniques using **LangChain**.

Text splitting is an important step in RAG (Retrieval-Augmented Generation) applications. It divides large documents into smaller chunks, making them easier to process, store, and retrieve.

## Topics Covered

- Character Text Splitter
- Recursive Character Text Splitter
- Language-Specific Text Splitter

## Key Concepts

**1. Chunk Size**

Defines the maximum target size of each text chunk. For example, `chunk_size=100` means each chunk should contain approximately 100 characters by default.

**2. Chunk Overlap**

Defines how much text should be repeated between consecutive chunks. It helps preserve context across chunk boundaries.

**3. Separators**

Define where the text should be split, such as newlines (`\n`), paragraphs (`\n\n`), or spaces.

## Project Structure

```text
langchain-text-splitters/
│
├── character_splitter.py
├── recursive_character_splitter.py
├── language_specific_splitter.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/JiyaSheikh06/langchain-text-splitters.git
```

Navigate to the project directory:

```bash
cd langchain-text-splitters
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run each Python file separately:

```bash
python character_splitter.py
python recursive_character_splitter.py
python language_specific_splitter.py
```

## Learning Objectives

- Understand different text-splitting strategies.
- Learn how chunk size and overlap affect splitting.
- Explore language-specific code splitting.
- Practice splitting PDF documents into LangChain Document chunks.
- Understand the role of text splitting in RAG pipelines.

## Technologies

- Python
- LangChain
- LangChain Community

---

**Purpose:** Learning and practicing LangChain text-splitting techniques through simple Python examples.

## 🤝 Feedback & Contributions

Suggestions, feedback, and discussions are always welcome!

If you find this repository useful, consider giving it a ⭐.

---

## 👩‍💻 Author

**Javairiya Naeem**

GitHub: [@JiyaSheikh06](https://github.com/JiyaSheikh06)