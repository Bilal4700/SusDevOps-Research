# extensions/GoogleCloudStorage.py

from google.cloud import storage
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

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

def write_string_to_gcs(
    object_name: str,
    data: str,
    folder: str = None,          # top-level folder (e.g., "OpenAi")
    subfolder: str = None,       
    content_type: str = "application/json"
) -> str:
    bucket = set_gcs_connection()

    # Build object path with optional folder and subfolder
    parts = []
    if folder:
        parts.append(folder.strip("/"))
    if subfolder:
        parts.append(subfolder.strip("/"))
    parts.append(object_name)

    object_path = "/".join(parts)

    blob = bucket.blob(object_path)
    blob.upload_from_string(data, content_type=content_type)
    return f"gs://{GCS_BUCKET}/{object_path}"
