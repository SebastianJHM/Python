import requests
response = requests.get('https://www.google.com')
print(response.text)
print(response.ok)
print(response.status_code)

p = {"description": "white kitten",
     "name": "Snowball",
     "age_months": 6}
response = requests.post("https://example.com/path/to/api", data=p)
print(response.request.url)
print(response.request.body)

response = requests.post("https://example.com/path/to/api", json=p)
print(response.request.url)
print(response.request.body)


## TALLER
#! /usr/bin/env python3

import os
import requests

for file_name in os.listdir("/data/feedback"):
    file  = open("/data/feedback/" + file_name,'r')
    data = [x for x in file.read().splitlines()]
    dict_info = {}
    dict_info["title"] = data[0]
    dict_info["name"] = data[1]
    dict_info["date"] = data[2]
    dict_info["feedback"] = data[3]
    print(dict_info)

    response = requests.post("http://35.184.90.87/feedback/" , json = dict_info)
    print(response.ok)
    print(response.status_code)
    print(response.request.url)
    print(response.request.body)
