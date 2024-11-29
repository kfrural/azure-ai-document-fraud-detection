from azure.storage.blob import BlobServiceClient

def get_blob_url(container_name, blob_name):
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    return blob_client.url

if __name__ == "__main__":
    print(get_blob_url("documents", "sample_doc.pdf"))
