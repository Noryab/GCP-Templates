from function.drive import Drive
# from function.storage import Storage


class FromDriveToStorage:
    
    def __init__(self, config, credentials=None) -> None:
        Drive(config=config().to_dict(), credentials=credentials)    
        # Storage(config().to_dict(), credentials=credentials)

    @classmethod
    def run(self,):

        files = Drive.search_file()
        # Storage.upload_to_bucket(files)
        pass
