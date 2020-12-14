#!/usr/bin/env python3
import os
from PIL import Image

path = "supplier-data/images/"

for im_name in os.listdir(path):
    name_file, extension = os.path.splitext(path + im_name)
    if extension == ".tiff":
        im = Image.open(path + im_name)
        im = im.resize((600, 400)).convert('RGB')
        im.save(name_file + ".jpeg","JPEG")