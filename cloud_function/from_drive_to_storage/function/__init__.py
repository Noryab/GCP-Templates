import os 
import google.auth

from google.oauth2 import service_account

from config import config_env

from function.function import  FromDriveToStorage


CONFIG_ENV = os.getenv("ENV") or "loc"
config = config_env[CONFIG_ENV]

if CONFIG_ENV=="loc":
    creds = service_account.Credentials.from_service_account_file('/home/portfolio/cloud_function/from_drive_to_storage/function/key_storage.json') # If you're using local machine    
    scoped_credentials = creds.with_scopes(config.SCOPES)    
else:
    creds, _ = google.auth.default() #If you're using a cloud function directly
    scoped_credentials = creds.with_scopes(config.SCOPES)


FromDriveToStorage(config, creds=creds, scoped_credentials=scoped_credentials)


def init_function() -> None:
    # Drive(config_env[config_name], scoped_credentials=scoped_credentials)
    pass