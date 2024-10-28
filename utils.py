import requests
import os

URL = 'http://localhost:3000/'
DATA_DIR = 'data/'

def upload_image(path):
    try:
        prev_images = set(os.listdir(DATA_DIR))
        req = {'images': open(path, 'rb')}
        res = requests.post(URL + 'uploadImages', files=req)
        new_images = set(os.listdir(DATA_DIR))
        assert len(new_images) == len(prev_images) + 1

        return (new_images - prev_images).pop(), res.json()
    except:
        raise Exception("Failed to upload image")

def delete_image(path):
    try:
        res = requests.delete(URL + f'deleteImage?imagePath={path}')
        return res.json()
    except:
        raise Exception("Failed to delete image")

def search_image(path):
    try:
        res = requests.get(URL + f'search?imagePath={path}')

        return {d['src']: d['score'] for d in res.json()}
    except:
        raise Exception("Failed to search image")