import os
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

def analyze_document(blob_url):
    endpoint = os.getenv("FORM_RECOGNIZER_ENDPOINT")
    key = os.getenv("FORM_RECOGNIZER_KEY")
    
    client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))
    poller = client.begin_analyze_document_from_url("prebuilt-document", blob_url)
    result = poller.result()

    data = {}
    for document in result.documents:
        for field, value in document.fields.items():
            data[field] = value.value
    return data

if __name__ == "__main__":
    extracted_data = analyze_document("<URL_do_blob>")
    print(extracted_data)
