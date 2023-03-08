import copy
import dataclasses
import inspect
import os

from dataclasses import field
from typing import List
from typing import Dict
from typing import Tuple

def default_field(obj):
    return field(default_factory=lambda: copy.copy(obj))

basedir = os.path.abspath(os.path.dirname(__file__))

@dataclasses.dataclass
class ConfigBase:

    SCOPES: List = default_field([                
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/drive.file',
        'https://www.googleapis.com/auth/drive.readonly',
        'https://www.googleapis.com/auth/drive.metadata.readonly',
        'https://www.googleapis.com/auth/drive.appdata',
        'https://www.googleapis.com/auth/drive.metadata',
        'https://www.googleapis.com/auth/drive.photos.readonly',
    ])
    TOKEN_URI: str ="https://www.googleapis.com/oauth2/v3/token"
    CLIENT_ID: str = '318040672941-jbi4pi3rhckhlcpv5cp32v0c01lofqml.apps.googleusercontent.com'
    CLIENT_SECRET: str = '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'
    REFRESH_TOKEN: str = '1//05xsP12DEWZXZCgYIARAAGAUSNwF-L9Ir4drRlGPutBcs38_SMPutB59uYVTeq0stwntC9ltYGSduWT5BZ1UJl6VUk1L5R4GDDrs'
    TOKEN: str = ""
    DEBUG: bool =True
    

@dataclasses.dataclass
class LocalConfig(ConfigBase):    
    
    BUCKET_NAME: str ="files_from_drive"
    DRIVE_PATH: str="files_to_storage"
    PROJECT_NAME: str ="portfolio"  
    
    @classmethod
    def from_dict(self, d):
        # super().SCOPES
        return self(**{
             k: v for k, v in d.items() 
             if k in inspect.signature(self).parameters
        })

    
    def to_dict(self):
        return dataclasses.asdict(self)        

@dataclasses.dataclass
class DevelopmentConfig(ConfigBase):  
            
    BUCKET_NAME: str ="bucket_drive_portfolio"
    DRIVE_PATH: str="files_to_storage"
    PROJECT_NAME: str ="kiosko-375015"  
           

    @classmethod
    def from_dict(self, d):        
        return self(**{
             k: v for k, v in d.items() 
             if k in inspect.signature(self).parameters
        })
    
    def to_dict(self):
        return dataclasses.asdict(self)

        return self(**d)

@dataclasses.dataclass
class ProductionConfig(ConfigBase):    

    BUCKET_NAME: str ="files_from_drive"
    DRIVE_PATH: str="files_to_storage"
    PROJECT_NAME: str ="portfolio"  

    DEBUG=False

    def __post_init__(self):
        super().__init__(self.side, self.side)



config_env = dict(loc=LocalConfig, dev=DevelopmentConfig, prod=ProductionConfig)
