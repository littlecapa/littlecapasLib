import os, zipfile, requests
from download import readZip

def unzip_twic_file(filename_zip, unzip_folder):
    with zipfile.ZipFile(filename_zip, 'r') as zip_file:
        zip_file.extractall(unzip_folder)
        os.remove(filename_zip)

def get_file_info(issue_number, base_url, twic_pattern):
    filename_zip = twic_pattern.replace("<<number>>", str(issue_number))
    return filename_zip, base_url+filename_zip

def download_twic_file(base_url, issue_number, download_dir, unzip_dir, twic_pattern):
    url, filename_zip = get_file_info(issue_number, base_url, twic_pattern)
    filename = os.path.join(download_dir, filename_zip)
    try:
        readZip(url = url, filename = os.path.join(download_dir, filename))
        unzip_twic_file(filename, unzip_dir)
    except Exception as ex:
        print ("error: ", str(ex.code))
        raise ex
    
def exist_twic_file(issue_number, base_url, twic_pattern):
    url, _ = get_file_info(issue_number, base_url, twic_pattern)
    try:
        response = requests.head(url, allow_redirects=True)
        # Check if the response status code indicates success (200 OK)
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Error checking file at {url}: {e}")
        return False
    
def get_highest_twic_issue(highest, base_url, twic_pattern):
    while exist_twic_file(highest+1, base_url, twic_pattern):
        highest += 1
    return highest