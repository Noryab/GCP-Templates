from function.drive import Drive
from function.storage import Storage


class FromDriveToStorage:
    
    def __init__(self, config, creds=None, scoped_credentials=None) -> None:
        Drive(config().to_dict(), scoped_credentials=scoped_credentials)    
        Storage(config().to_dict(), creds=creds)

    @classmethod
    def run(self,):

        files = Drive.search_file()
        Storage.upload_to_bucket(files)
        pass
