import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
      return {
          'Content-Type': 'application/json',
          'Autorization': f'OAuth {self.token}'       
      }

def upload(self, disk_file_path: str):
    files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
    headers = self.get_headers()
    params = {'path': disk_file_path, 'overwrite': 'true'}
    response = requests.get(files_url, headers=headers, params=params)
    print(response.json())
    return response.json()

def upload_file_to_disk(self, disk_file_path, filename):
    href = self.upload(disk_file_path=disk_file_path).get('href', '')
    response = requests.put(href, data=open(filename, 'rb'))
    response.raise_for_status()
    if response.status_code == 201:
        print('успешно')
      
 
if __name__ == '__main__':
    path_to_file = ('netology/test.txt', 'test.txt')
    token = 'y0_AgAAAABadk2tAADLWwAAAADTgxJMxtuvJnygS-iv9TrBtvZEAZxVEzw'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)