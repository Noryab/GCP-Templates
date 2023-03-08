import inspect
import io

import dataclasses
from dataclasses import dataclass, field
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


@dataclass
class Drive:
    service: object = field(default=None)
    credentials: object = field(default=None)
    config: object = field(default_factory={})
    

    @classmethod    
    def update(cls, key, value):
        setattr(cls, key, value)

    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                self.update(key, dictionary[key])
        for key in kwargs:
            self.update( key, kwargs[key])
        
        self._get_gdrive_service()

    def _get_gdrive_service(self):
        self.credentials = Credentials(
            token=self.config["TOKEN"],
            refresh_token=self.config["REFRESH_TOKEN"],
            token_uri=self.config["TOKEN_URI"],
            client_id=self.config["CLIENT_ID"],
            client_secret=self.config["CLIENT_SECRET"],
        )
        self.credentials.refresh(Request())
        self.config["TOKEN"] = self.credentials.token                                        
        self.update('service', build('drive', 'v3', credentials=self.credentials))                    
        

    def to_dict(self):
        return dataclasses.asdict(self)        


    @classmethod
    def search_file(self, request = None):
        
        files = []
        page_token = None
        file_to_download = None
        # objects_list = get_blobs()
        # while True:
        # response = self.service.files().list(
        #                                         q=f"mimeType != 'application/vnd.google-apps.folder'",
        #                                         fields = 'nextPageToken, ''files(id,name)',
        #                                         pageToken=page_token
        #                                     ).execute()
        response = self.service.files().list().execute()

        print(response.get("files",[]))
        return response
        #     for file in response.get('files', []):
        #         print(F'Found file: {file.get("name")}, {file.get("id")}')
        #         file_id = file.get("id")
        #         file_name = file.get("name")
        #         if file_name not in objects_list:
        #             request = self.service.files().get_media(fileId=file_id)
        #             file_download_buffer = io.BytesIO()
        #             downloader = MediaIoBaseDownload(file_download_buffer, request)
        #             done = False
        #             while done is False:
        #                 status, done = downloader.next_chunk()
        #                 print(F'Download {int(status.progress() * 100)}.')
                    
        #             upload_to_drive(file_download_buffer,file_name)

        #     files.extend(response.get('files', []))
        #     page_token = response.get('nextPageToken', None)


        #     if page_token is None:
        #         break
