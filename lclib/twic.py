import os, zipfile
from download import readZip

class TwicWorker:
    """
    A class to handle TWIC (The Week in Chess) tasks.
    This worker can download, process, and manage TWIC files.
    """

    def __init__(self, base_url: str, twic_pattern: str, download_dir: str, unzip_dir: str):
        """
        Initialize the TWIC worker.

        Args:
            base_url (str): The base URL for downloading TWIC files.
            download_dir (str): The directory where TWIC files will be stored.
        """
        self.base_url = base_url.rstrip("/")
        self.download_dir = download_dir
        self.twic_pattern = twic_pattern
        self.unzip_dir = unzip_dir
        os.makedirs(self.download_dir, exist_ok=True)
        os.makedirs(self.unzip_dir, exist_ok=True)

    def unzip_twic_file(self, filename_zip, unzip_folder):
        with zipfile.ZipFile(filename_zip, 'r') as zip_file:
            zip_file.extractall(unzip_folder)
            os.remove(filename_zip)

    def download_twic_file(self, issue_number: int):
        """
        Download a TWIC file for a given issue number.

        Args:
            issue_number (int): The TWIC issue number to download.

        """
        filename_zip = self.twic_pattern.replace("<<number>>", str(issue_number))
        filename = os.path.join(self.download_dir, filename_zip)
        url = self.base_url+filename_zip
        try:
            readZip(url = url, filename = os.path.join(self.download_dir, filename))
            self.unzip_twic_file(filename, self.unzip_dir)
        except Exception as ex:
            print ("error: ", str(ex.code))
            raise ex