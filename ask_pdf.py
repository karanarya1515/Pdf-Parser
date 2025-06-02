import subprocess

def ask_mistral(question, context):
    prompt = f"Answer the question based on the context.\n\nContext:\n{context}\n\nQuestion:\n{question}"
    command = ["ollama", "run", "mistral", prompt]
    output = subprocess.run(command, capture_output=True, text=True)
    return output.stdout.strip()
