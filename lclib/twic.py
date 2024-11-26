import os, zipfile, requests
from download import readZip

def unzip_twic_file(self, filename_zip, unzip_folder):
    with zipfile.ZipFile(filename_zip, 'r') as zip_file:
        zip_file.extractall(unzip_folder)
        os.remove(filename_zip)

def get_file_info(self, issue_number):
    filename_zip = self.twic_pattern.replace("<<number>>", str(issue_number))
    return filename_zip, self.base_url+filename_zip

def download_twic_file(self, issue_number: int):
    """
    Download a TWIC file for a given issue number.

    Args:
        issue_number (int): The TWIC issue number to download.

    """
    url, filename_zip = self.get_file_info(issue_number)
    filename = os.path.join(self.download_dir, filename_zip)
    try:
        readZip(url = url, filename = os.path.join(self.download_dir, filename))
        self.unzip_twic_file(filename, self.unzip_dir)
    except Exception as ex:
        print ("error: ", str(ex.code))
        raise ex
    
def exist_twic_file(self, issue_number: int):
    url, _ = self.get_file_info(issue_number)
    try:
        response = requests.head(url, allow_redirects=True)
        # Check if the response status code indicates success (200 OK)
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Error checking file at {url}: {e}")
        return False
    
def get_highest_twic_issue(self):
    highest = self.last_issue
    while self.exist_twic_file(highest+1):
        highest += 1
    return highest