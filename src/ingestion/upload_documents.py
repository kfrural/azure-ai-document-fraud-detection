import os
from azure.storage.blob import BlobServiceClient

def upload_document(file_path, container_name):
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=os.path.basename(file_path))
    
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data)
        print(f"Uploaded {file_path} to container {container_name}")

if __name__ == "__main__":
    upload_document("data/samples/sample_doc.pdf", "documents")
