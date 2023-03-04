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

    DEBUG: bool =True
    

@dataclasses.dataclass
class LocalConfig(ConfigBase):    

    name: str= field(default=None)    
    active: str= field(default=1)    
    catalog: float= field(default=None)    
    values: str= field(default=None)        
    uid: str = field(default=None)        

    BUCKET_NAME: str ="files_from_drive"
    DRIVE_PATH="files_to_storage"
    PROJECT_NAME="portfolio"
    
    
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
        
    name: str= field(default=None)    
    active: str= field(default=1)    
    catalog: float= field(default=None)    
    values: str= field(default=None)        
    uid: str = field(default=None)        

    BUCKET_NAME: str ="files_from_drive"
    DRIVE_PATH="files_to_storage"
    PROJECT_NAME="portfolio"
           

    @classmethod
    def from_dict(self, d):        
        return self(**{
             k: v for k, v in d.items() 
             if k in inspect.signature(self).parameters
        })
    
    def to_dict(self):
        return dataclasses.asdict(self)

        return self(**d)


class ProductionConfig(ConfigBase):    
    BUCKET_NAME=""
    DRIVE_PATH=""
    PROJECT_NAME=""

    DEBUG=False

    def __post_init__(self):
        super().__init__(self.side, self.side)



config_env = dict(loc=LocalConfig, dev=DevelopmentConfig, prod=ProductionConfig)
