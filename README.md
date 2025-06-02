<<<<<<< HEAD

# 📄 PDF Question Answering System using Mistral (Ollama)

A local, privacy-friendly question answering system that reads a PDF, breaks it into chunks, stores embeddings using FAISS, and uses a local Mistral model (via Ollama) to answer user questions.

---

## 🛠️ Tools & Technologies

| Tool / Library        | Use / Role                                                                 |
|-----------------------|----------------------------------------------------------------------------|
| **Python**            | Main programming language                                                  |
| **PyMuPDF (fitz)**    | Extracts text content from PDF files                                       |
| **Langchain**         | Handles chunking, embedding, vector search, and LLM prompting              |
| **FAISS**             | Vector store for fast similarity search                                    |
| **Ollama**            | Local model runner for Mistral                                             |
| **Mistral**           | Lightweight open-source LLM used for answering questions                   |

---

## 📦 Project Structure

```
PDF-QA-Project/
│
├── main.py              # Entry point: load PDF, process, ask questions
├── read_pdf.py          # Handles PDF text extraction & chunking
├── vector_store.py      # Embeds and stores chunks using FAISS
├── ask_pdf.py           # Handles question answering using Langchain & Mistral
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

---

## 🧠 How It Works

1. **Extract PDF Text**: Uses PyMuPDF to read the file contents.
2. **Chunking**: Splits long text into smaller sections for context management.
3. **Embedding**: Each chunk is embedded using a Langchain-compatible embedding model.
4. **FAISS Vector Store**: Stores the embeddings for fast similarity search.
5. **Ask a Question**: User inputs a natural language question.
6. **Retriever**: Retrieves the most relevant chunks using FAISS.
7. **Mistral (via Ollama)**: Uses retrieved context to answer the question.
8. **Output**: Answer is printed in the terminal.

---

## ▶️ How to Run

### 1. Install Requirements
```bash
pip install -r requirements.txt
```

### 2. Install Ollama and Run Mistral
```bash
# Install ollama (if not already)
curl -fsSL https://ollama.com/install.sh | sh

# Pull and run Mistral
ollama pull mistral
ollama run mistral
```

### 3. Run the Project
```bash
python main.py
```

---

## 🧪 Example Usage

```text
Ask a question (or type 'exit'): What is the course breakdown?
Answer:
- The course includes fundamentals of AI, Python basics, project work, and assignments...
```

---

## 📌 Notes

- Mistral runs locally — no internet or API keys required.
- Make sure you have **at least 6 GB RAM** to run Mistral smoothly.
- You can swap Mistral with other Ollama-supported models (like LLaMA3).

---

## 🤖 Future Improvements

- Add web UI (Streamlit or Gradio)
- Multi-file PDF support
- Save conversation history
=======
# Pdf-Parser
>>>>>>> d4e151096fdaf83784f511340f735448272cbc2b
