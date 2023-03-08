from dataclasses import dataclass, field
from google.cloud import storage
from google.cloud.storage import Blob


@dataclass
class Storage:
    client: object = field(default=None)
    credentials: object = field(default=None)  
    PROJECT_NAME: str = field(default="")  
    BUCKET_NAME: str = field(default="")  

    @classmethod    
    def update(cls, key, value):
        setattr(cls, key, value)

    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                self.update(key, dictionary[key])
        for key in kwargs:
            self.update( key, kwargs[key])    
        self.update( "client", storage.Client(self.PROJECT_NAME, self.credentials))    
        self.update( "bucket", self.client.get_bucket(self.BUCKET_NAME))    
        
    @classmethod
    def get_blobs(self):        
        objects_in_bucket = self.client.list_blobs(self.bucket, fields='items(name)')
        object_names = []
        for object in objects_in_bucket:
            object_names.append(object.name)
        return object_names
    

    @classmethod
    def upload_to_bucket(self, files):                
        for file in files:
            file_name = file["file_name"]
            blob = Blob(file_name, self.bucket)
            blob.upload_from_file(file, rewind=True)
