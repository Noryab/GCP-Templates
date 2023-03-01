import os 
import google.auth

# from google.oauth2 import service_account

from config import config_env

from function.function import  FromDriveToStorage
import google.auth

# Create credentials with Drive & BigQuery API scopes.
# Both APIs must be enabled for your project before running this code.
# credentials, project = google.auth.default(
#     scopes=[        
#         'https://www.googleapis.com/auth/drive',
#     ]
# )


CONFIG_ENV = os.getenv("ENV") or "dev"
config = config_env[CONFIG_ENV]

# if CONFIG_ENV=="loc":
#     creds = service_account.Credentials.from_service_account_file('/home/portfolio/GCP-Templates/cloud_function/from_drive_to_storage/function/key_storage.json') # If you're using local machine    
#     scoped_credentials = creds.with_scopes(config.SCOPES)    
# else:
creds, _ = google.auth.default()
scoped_credentials = creds.with_scopes(config.SCOPES)


FromDriveToStorage(config, creds=creds, scoped_credentials=scoped_credentials)
