#!/usr/bin/env python3

# Script-name:  changeImage.py

# EDEN: This script modifies the image according to these requirements:  
#   - Size: Change image resolution from 3000x2000 to 600x400 pixel      
#   - Format: Change image format from .TIFF to .JPEG
#   - Additional: Convert RGBA to RGB
#   - Additional: After processing the images, save them in '~/supplier-data/images'


#--------------------------------------------START OF CODE---------------------------------------------#

import os
from PIL import Image

# Saves username to a variable
usernam = os.getenv('USER')

# Saves images directory to a variable
imagedir = "/home/{}/supplier-data/images/".format(usernam)

# Iterates over the images in images directory
for file in os.listdir(imagedir):

    # Modifies to .JPEG -- only the .tiff files
    if file.endswith("tiff"):
        oldimg = imagedir + file
        path = os.path.splitext(oldimg)[0]
        newimg = "{}.jpeg".format(path)

        # Changes size and convert to RGB
        im = Image.open(oldimg)
        im.resize((600, 400)).convert("RGB").save(newimg, "JPEG")        
        im.close()


#------------------------------------------------END OF CODE------------------------------------------------#
