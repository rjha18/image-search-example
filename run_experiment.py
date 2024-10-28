from utils import *
import os

DATA_DIR = 'data/'
ADV_DIR = 'adv_images/'

for adv in os.listdir(ADV_DIR):
    new_path, _ = upload_image(ADV_DIR + adv)
    print(new_path)
    for image in os.listdir(DATA_DIR):
        print(search_image(DATA_DIR + image))
        input()
    delete_image(ADV_DIR + new_path)
