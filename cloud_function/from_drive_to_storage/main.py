from function import init_function
from function.function import FromDriveToStorage


def function_gcp():
    FromDriveToStorage.run()

if __name__ == "__main__":
    function_gcp()
    # drive = Drive()
    # storage = StorageGCP()
    # storage.upload_to_bucket(drive.search_file())