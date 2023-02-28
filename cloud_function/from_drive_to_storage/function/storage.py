from dataclasses import dataclass
from google.cloud import storage
from google.cloud.storage import Blob


@dataclass
class Storage:
    client: object
    creds: object    

    @classmethod    
    def update(cls, key, value):
        setattr(cls, key, value)

    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                self.update(key, dictionary[key])
        for key in kwargs:
            self.update( key, kwargs[key])

    def __post_init__(self) -> None:
        self.client = storage.Client(self.PROJECT_NAME,self.creds)         

    def get_blobs(self, bucket_name):        
        bucket_name = self.client.get_bucket(bucket_name)
        objects_in_bucket = self.client.list_blobs(bucket_name, fields='items(name)')
        object_names = []
        for object in objects_in_bucket:
            object_names.append(object.name)
        return object_names
    
    def upload_to_bucket(self, file, file_name, bucket_name):        
        bucket_name = self.client.get_bucket(bucket_name)
        blob = Blob(file_name, bucket_name)
        blob.upload_from_file(file, rewind=True)
