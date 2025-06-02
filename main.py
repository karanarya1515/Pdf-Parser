from read_pdf import read_pdf, chunk_text
from vector_store import build_index, search
from ask_pdf import ask_mistral

if __name__ == "__main__":
    file_path = r"C:\Users\karan\OneDrive\Desktop\PDF Extractor - AI Project\Assignment Guidelines_Program Essentials_Pradeepta Mishra_Assignment 2.pdf"
    text = read_pdf(file_path)
    chunks = chunk_text(text)
    build_index(chunks)

    while True:
        question = input("\nAsk a question (or type 'exit'): ")
        if question.lower() == "exit":
            break
        top_chunks = search(question)
        context = "\n\n".join(top_chunks)
        answer = ask_mistral(question, context)
        print("\nAnswer:\n", answer)
