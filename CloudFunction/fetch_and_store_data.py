import requests
from google.cloud import storage
import os

def fetch_and_store_data(request):
    # Configuration
    api_url = 'https://example.com/api/data'
    bucket_name = 'your-bucket-name'
    blob_name = 'data-file.json'

    # Fetch data from API
    response = requests.get(api_url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    data = response.text

    # Initialize Cloud Storage client
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    # Upload data to Google Cloud Storage
    blob.upload_from_string(data)

    return 'Data fetched and stored successfully.'
