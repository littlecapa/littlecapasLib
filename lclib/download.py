import requests, time
from urllib.error import HTTPError

def readZip(url, file_name_zip, attempts=1):

    # User Agent is required by TWIC / see https://deviceatlas.com/blog/list-of-user-agent-strings
    ua = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7)'
    for attempt in range(1, attempts+1):
        try:
            print("Try ", url)
            if attempt > 1:
                time.sleep(10)  # 10 seconds wait time between downloads
            with requests.get(url, headers={"User-Agent": ua}, stream=True) as response:
                print ("Status: ", response.status_code)
                if response.status_code == HTTPError:
                    print ("Ende")
                    return True
                response.raise_for_status()
                with open(file_name_zip, 'wb') as out_file:
                    print("File open")
                    for chunk in response.iter_content(chunk_size=1024*1024):  # 1MB chunks
                        out_file.write(chunk)
                print("Success")

        except Exception as ex:
            print("Error: ", str(ex))
            raise ex

  with zipfile.ZipFile(file, 'r') as zip_file:
    zip_file.extractall(folder)
    os.remove(file)
  # Noch nicht zu Ende
  return False
