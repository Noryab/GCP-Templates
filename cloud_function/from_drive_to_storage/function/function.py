from function.drive import Drive
from function.storage import Storage


class FromDriveToStorage:
    
    def __init__(self, config, credentials=None) -> None:
        Drive(config_data=config().to_dict())    
        Storage(config().to_dict(), credentials=credentials)

    @classmethod
    def run(self,):

        response = Drive.search_files()
        Storage.upload_to_bucket(response)
        pass
