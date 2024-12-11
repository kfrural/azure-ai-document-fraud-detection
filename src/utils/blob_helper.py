from azure.storage.blob import BlobServiceClient
import os

def get_blob_url(container_name, blob_name):
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    if not connection_string:
        raise ValueError("AZURE_STORAGE_CONNECTION_STRING não configurado")
    
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    return blob_client.url

if __name__ == "__main__":
    try:
        print(get_blob_url("documents", "sample_doc.pdf"))
    except Exception as e:
        print(f"Erro ao obter o URL do blob: {str(e)}")
