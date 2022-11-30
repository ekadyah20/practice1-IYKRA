# Input alas dan tinggi segitiga
from google.cloud import storage
import urllib.request
project_id = 'fluid-stratum-370010'
bucket_name = 'practice1-df8'
destination_blob_name = 'upload.test'
storage_client = storage.Client.from_service_account_json('fluid-stratum-370010-5fcfba31486a.json')

# This works fine
#source_file_name = 'localfile.txt'

# When using a remote URL I get 'IOError: [Errno 2] No such file or directory'
source_file_name = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Gingerbread_House_Essex_CT.jpg/220px-Gingerbread_House_Essex_CT.jpg'

def upload_blob(bucket_name, source_file_name, destination_blob_name):   
    link = urllib.request.urlopen(source_file_name)

    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_string(link.read(), content_type='image/jpg')

upload_blob(bucket_name, source_file_name, destination_blob_name)