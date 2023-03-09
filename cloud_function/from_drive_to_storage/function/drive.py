import inspect
import io

import dataclasses
from dataclasses import dataclass, field
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload


@dataclass
class CredentialsDrive:
    TOKEN: str
    REFRESH_TOKEN: str
    TOKEN_URI: str
    CLIENT_ID: str
    CLIENT_SECRET: str

    @classmethod
    def from_dict(self, d):
        return self(**{
             k: v for k, v in d.items() 
             if k in inspect.signature(self).parameters
        })


    def get_credentials(self):
        credentials = Credentials(
            token= self.TOKEN,
            refresh_token= self.REFRESH_TOKEN,
            token_uri= self.TOKEN_URI,
            client_id= self.CLIENT_ID,
            client_secret= self.CLIENT_SECRET,
        )
        credentials.refresh(Request())
        return credentials


@dataclass
class Drive:
    credentials: CredentialsDrive
    service: object = field(init=False)

    def __init__(self, config_data) -> None:
        type(self).credentials = CredentialsDrive.from_dict(config_data)                    
        type(self).service = build('drive', 'v3', credentials=self.credentials.get_credentials())
    
    @classmethod
    def search_files(cls, query=None, page_token=None):
        try:
            return cls.service.files().list(q=query,
                                                fields = 'nextPageToken, ''files(id, name, mimeType, modifiedTime)',
                                                pageToken=page_token).execute()
            
        except HttpError as error:
            print(f'An error occurred: {error}')
            return None

    @classmethod
    def download_file_by_id(cls, file_id):
        request = cls.service.files().get_media(fileId=file_id)
        file_download_buffer = io.BytesIO()
        downloader = MediaIoBaseDownload(file_download_buffer, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print(F'Download {int(status.progress() * 100)}.')
        return file_download_buffer

    def to_dict(self):
        return dataclasses.asdict(self)
