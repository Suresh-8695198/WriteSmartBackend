# firebase_storage.py
from google.cloud import storage
import uuid

# Initialize Firebase Storage
bucket = storage.bucket()

def upload_image_to_firebase(image_file):
    try:
        blob = bucket.blob(f"images/{uuid.uuid4()}.jpg")
        blob.upload_from_file(image_file, content_type=image_file.content_type)
        blob.make_public()
        return blob.public_url
    except Exception as e:
        print("Error uploading image:", e)
        return None
