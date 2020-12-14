#!/usr/bin/env python3
import os
import requests

path_images = "supplier-data/images/"
path_description = "supplier-data/descriptions/"
url = "http://localhost/upload/"

for direction in os.listdir(path_description):
    file  = open(path_description + direction,'r')
    data = [x for x in file.read().splitlines() if x != '']
    keys = ["name", "weight", "description"]
    dict_info = dict(zip(keys, data))
    dict_info["weight"] = int(dict_info["weight"][0:-4])
    dict_info["image_name"] = os.path.splitext(direction)[0] + ".jpeg"
    print(dict_info)
    
    response = requests.post("http://34.67.22.6/fruits/" , json = dict_info)