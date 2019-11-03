import requests
import shutil

def download(url, name):
    stream = (requests.get(url, stream=True))
    with open(name, 'wb+') as file:
        shutil.copyfileobj(stream.raw, file)
