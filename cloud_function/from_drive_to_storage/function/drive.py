import inspect
import io

import dataclasses
from dataclasses import dataclass, field
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from oauth2client import client, file, tools


@dataclass
class Drive:
    service: object = field(default=None)
    scoped_credentials: object = field(default=None)
    scopes: object = field(default=None)
    config: object = field(default=None)

    @classmethod    
    def update(cls, key, value):
        setattr(cls, key, value)

    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                self.update(key, dictionary[key])
        for key in kwargs:
            self.update( key, kwargs[key])

        if self.scoped_credentials:
            self.update('service', self._get_gdrive_service())        
            # object.__setattr__(self, 'service', build('drive', 'v3', credentials=self.scoped_credentials))        

    def _get_gdrive_service(self):

        import pickle
        import os

        creds=None

        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.config["SCOPES"])
                # creds = flow.run_local_server(port=0)
                name ="a"            
                storage = file.Storage(name + ".dat")
                creds = tools.run_flow(flow, storage)

            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        
        name ="a"
        storage = file.Storage(name + ".dat")
        creds = tools.run_flow(flow, storage)
        return build('drive', 'v3', credentials=creds)



    def to_dict(self):
        return dataclasses.asdict(self)
        return dataclasses.asdict(self, dict_factory=lambda x: {k: v for (k, v) in x if v is not None})


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
