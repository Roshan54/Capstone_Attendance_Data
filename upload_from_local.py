import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Set the connection string to your storage account
connection_string = "DefaultEndpointsProtocol=https;AccountName=facerecognitioncapstone;AccountKey=DayqekRI//ZUtjMKwsq+LhIWPzlaJ53LcBepkVLTNl028QXziXp/1appbdR7fB4Zhizba2YpANb++AStnTNKZA==;EndpointSuffix=core.windows.net"


# Set the container name and create a client object
container_name = "facercgntn"
container_client = ContainerClient.from_connection_string(connection_string, container_name)

# Set the local folder path
local_folder_path = r"C:\Users\bismi\Desktop\faceRecognitionCapstone\Images"

# List all the files in the local folder
for root, dirs, files in os.walk(local_folder_path):
    for file in files:
        # Set the blob name
        blob_name = os.path.join(root.replace(local_folder_path, ""), file).lstrip("\\")

        # Set the local file path
        local_file_path = os.path.join(root, file)

        # Create a blob client object
        blob_client = container_client.get_blob_client(blob_name)

        # Upload the file to the blob container
        with open(local_file_path, "rb") as data:
            blob_client.upload_blob(data)