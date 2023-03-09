import os 
import google.auth

from config import config_env
from function.function import  FromDriveToStorage

CONFIG_ENV = os.getenv("ENV") or "dev"
config = config_env[CONFIG_ENV]

credentials=None
credentials, project = google.auth.default(scopes=config().SCOPES)
FromDriveToStorage(config, credentials=credentials)



