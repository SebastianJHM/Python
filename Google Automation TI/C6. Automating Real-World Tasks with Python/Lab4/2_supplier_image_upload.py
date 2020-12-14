#!/usr/bin/env python3
import os
import requests

path_images = "supplier-data/images/"
url = "http://localhost/upload/"

for direction in os.listdir(path_images):
    name_file, extension = os.path.splitext(path_images + direction)
    if extension == ".jpeg":
        opened = open(path_images + direction, 'rb')
        r = requests.post(url, files={'file': opened})