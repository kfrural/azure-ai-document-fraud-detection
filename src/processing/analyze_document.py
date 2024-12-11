import os
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

def analyze_document(blob_url):
    endpoint = os.getenv("FORM_RECOGNIZER_ENDPOINT")
    key = os.getenv("FORM_RECOGNIZER_KEY")
    
    if not endpoint or not key:
        raise ValueError("Ambiente não configurado. Verifique FORM_RECOGNIZER_ENDPOINT e FORM_RECOGNIZER_KEY.")

    client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))
    poller = client.begin_analyze_document_from_url("prebuilt-document", blob_url)
    result = poller.result()

    data = {}
    for document in result.documents:
        for field, value in document.fields.items():
            data[field] = value.value
    return data

if __name__ == "__main__":
    try:
        extracted_data = analyze_document("<URL_do_blob>") #alterar aqui
        print(extracted_data)
    except Exception as e:
        print(f"Erro ao analisar o documento: {str(e)}")
