from azure.storage.blob import BlobServiceClient, BlobClient , ContainerClient
import face_recognition
import numpy as np
import cv2
import pickle
encodeList =[]
studentIds =[]
# Set the connection string to your storage account
connection_string = "DefaultEndpointsProtocol=https;AccountName=facerecognitioncapstone;AccountKey=DayqekRI//ZUtjMKwsq+LhIWPzlaJ53LcBepkVLTNl028QXziXp/1appbdR7fB4Zhizba2YpANb++AStnTNKZA==;EndpointSuffix=core.windows.net"

# Set the container name
container_name = "facercgntn"

# Create a blob service client object
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Create a container client object
container_client = blob_service_client.get_container_client(container_name)

# List all blobs in the container
blobs_list = container_client.list_blobs()

for blob in blobs_list:
    # Get a blob client object
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob.name)
    studentId = int(blob.name.replace(".png", ""))
    studentIds.append(studentId)
    image_data = blob_client.download_blob().content_as_bytes()
    nparr = np.frombuffer(image_data, np.uint8)
    imgStudent = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(imgStudent, cv2.COLOR_BGR2RGB)
    encode = face_recognition.face_encodings(img)[0]
    encodeList.append(encode)

# print(encodeList)
# print(studentIds)
encodeListKnownWithIds = [encodeList, studentIds]
# print(encodeListKnownWithIds)
file = open("Encode.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")