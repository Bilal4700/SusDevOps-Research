# extensions/GoogleCloudStorage.py

from google.cloud import storage
from pathlib import Path
from dotenv import load_dotenv
import os
# Ensure the required environment variables are set
if not os.environ.get("GCS_BUCKET"):
    raise EnvironmentError("GCS_BUCKET not set in environment variables")
if not os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"):
    raise EnvironmentError("GOOGLE_APPLICATION_CREDENTIALS not set in environment variables")

load_dotenv(override=True)

GCS_BUCKET = os.environ.get("GCS_BUCKET")
GOOGLE_APPLICATION_CREDENTIALS = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")


#  GOOGLE CLOUD STORAGE Connection
def set_gcs_connection():
    """Return a Google Cloud Storage client using the service account key from .env."""
    creds_path = GOOGLE_APPLICATION_CREDENTIALS
    if not creds_path:
        raise RuntimeError("GOOGLE_APPLICATION_CREDENTIALS not set in .env")

    if not Path(creds_path).is_file():
        raise FileNotFoundError(f"GCP credentials file not found at: {creds_path}")
    
    client = storage.Client.from_service_account_json(str(creds_path))
    bucket = client.bucket(GCS_BUCKET)
    return bucket

def write_string_to_gcs(object_name: str, data: str, content_type="application/json") -> str:
    bucket = set_gcs_connection()
    blob = bucket.blob(object_name)
    blob.upload_from_string(data, content_type=content_type)
    return f"gs://{GCS_BUCKET}/{object_name}"
