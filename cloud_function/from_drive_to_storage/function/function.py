import io 
import datetime as dt
from function.drive import Drive
from function.storage import Storage
from googleapiclient.http import MediaIoBaseDownload
from datetime import datetime
from datetime import timedelta

#Sumar dos días a la fecha actual

class FromDriveToStorage:
    last_run: dt = datetime.now().date().replace(day=1)

    def __init__(self, config, credentials=None) -> None:
        Drive(config_data=config().to_dict())    
        Storage(config().to_dict(), credentials=credentials)
        

    @classmethod
    def run(cls,):
        files = []        
        page_token = None
        
        filetype = "text/csv"
        query=f"(modifiedTime > '{cls.last_run}T12:00:00') AND (mimeType='{filetype}')"
        print(query)
        while True:
            response = Drive.search_files(query=query,page_token=page_token)          
            print(response)  
            
            for file in  response.get('files', []):
                print(F'Found file: {file.get("name")}, {file.get("id")}, {file.get("modifiedTime")}')
                modified_time = file.get("modifiedTime")
                if datetime.strptime(modified_time, "%Y-%m-%dT%H:%M:%S.%f%z").date()<=cls.last_run:
                    continue

                file_id = file.get("id")
                file_name = file.get("name")            
                file_download_buffer = Drive.download_file_by_id(file_id=file_id)
                Storage.upload_file_to_bucket(file_download_buffer,file_name)                

            files.extend(response.get('files', []))
            page_token = response.get('nextPageToken', None)

            if page_token is None:
                break
