import os
from azure.storage.blob import BlobServiceClient
from pathlib import Path

def upload_documents(directory, container_name):
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    
    directory_path = Path(directory)
    files_to_upload = [f for f in directory_path.iterdir() if f.is_file()]
    
    container_client = blob_service_client.get_container_client(container=container_name)
    if not container_client.exists():
        container_client.create_container()
    
    print(f"Encontrados {len(files_to_upload)} arquivos para upload.")
    
    for file in files_to_upload:
        try:
            with open(file, "rb") as data:
                blob_name = os.path.basename(file)
                blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
                blob_client.upload_blob(data, overwrite=True)
                print(f"Uploaded {file} to container {container_name}")
        except Exception as e:
            print(f"Erro ao uploadar {file}: {str(e)}")

if __name__ == "__main__":
    directory = "data/samples/"
    container_name = "documents"
    
    upload_documents(directory, container_name)
