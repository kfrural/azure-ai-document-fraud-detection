import os

def validate_document(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
    if not file_path.lower().endswith((".pdf", ".jpg", ".png")):
        raise ValueError("Tipo de arquivo não suportado. Apenas PDF, JPG e PNG são aceitos.")
    print(f"Documento válido: {file_path}")

if __name__ == "__main__":
    validate_document("data/samples/sample_doc.pdf")
