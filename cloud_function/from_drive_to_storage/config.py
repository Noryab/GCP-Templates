import os
import inspect

basedir = os.path.abspath(os.path.dirname(__file__))

class ConfigBase:
    SCOPES = ['https://www.googleapis.com/auth/drive']
    DEBUG=True
    

import dataclasses
import inspect

from dataclasses import field

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
        return self(**{
             k: v for k, v in d.items() 
             if k in inspect.signature(self).parameters
        })

    def to_dict(self):
        return dataclasses.asdict(self)
        return self(**d)

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



config_env = dict(loc=LocalConfig, dev=DevelopmentConfig, prod=ProductionConfig)
