import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
      return {
          'Content-Type': 'application/json',
          'Autorization': f'OAuth {self.token}'       
      }

def upload(self, file_path: str):
    files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
    headers = self.get_headers()
    params = {'path': file_path, 'overwrite': 'true'}
    response = requests.get(files_url, headers=headers, params=params)
    print(response.json())
    return response.json()
      
 
if __name__ == '__main__':
    path_to_file = ('C:\Users\minot\Desktop\HTTP\test.txt')
    token = 'y0_AgAAAABadk2tAADLWwAAAADTgxJMxtuvJnygS-iv9TrBtvZEAZxVEzw'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)