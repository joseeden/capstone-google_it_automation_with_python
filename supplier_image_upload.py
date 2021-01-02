#!/usr/bin/env python3

# Script-name:  supplier_image_upload.py  

# EDEN: This script uploads images in ~/suppliers-data/images to the 
# web server fruit catalog


#--------------------------------------------START OF CODE---------------------------------------------#


import requests, os    

# This is where the image will be uploaded.
url = "http://localhost/upload/"

# Saves username to a variable
usernam = os.getenv('USER')

# Saves images directory to a variable
imagedir = "/home/{}/supplier-data/images/".format(usernam)

# Iterates over the image directory and gets only the .JPEG files
for file in os.listdir(imagedir):
    if file.endswith("jpeg"):
        imagepath = imagedir + file
        with open(imagepath, 'rb') as opened:
            r = requests.post(url, files={'file': opened})


#------------------------------------------------END OF CODE------------------------------------------------#
