#!/usr/bin/env python3

# Script-name:  run.py

# EDEN: This script processes the .txt files (named 001.txt, 002.txt, ...) in the supplier-data/descriptions/
# directory and save them in a data structure so that you can then upload them via JSON. 
#   name
#   weight (in lbs)
#   description


#--------------------------------------------START OF CODE---------------------------------------------#

import os, requests, json

# Returns a list of dictionaries that contains name, weight(integer), description, image filename.
def catalog(url,descdir):
    fruit = {}

    # Iterates over the description .txt files
    for text in os.listdir(descdir):
        file = os.path.join(descdir,text)
        fruit.clear()

        # Opens each .txt file
        with open(file) as f:

            # Puts all the contents of the .txt into a single list.
            line = f.readlines()

            # Gets only the 'description' and ignore the fruit-name and weight
            # Replaces the unnecessary '\xa0' with a normal space ' '.
            # Then removes the next-line characters in the description
            description = line[2].replace(u"\xa0", u" ").strip("\n") 

            # Fill-in the dictionary with the required values.
            fruit["description"] = description
            fruit["weight"] = int(line[1].strip('\n').strip('lbs'))
            fruit["name"] = line[0].strip('\n')
            fruit["image_name"] = (text.strip('.txt')) + '.jpeg'
            
            print(fruit)

            # Uploads the fruits dictionary in json format to the URL and gets the response.
            if url != "":
                response = requests.post(url, json=fruit)
                print(response.request.url)
                print(response.status_code)

    return 0
        
if __name__=='__main__':
    
    # Django REST Framework
    url = 'http://localhost/fruits/'
    usernam = os.getenv('USER')
    
    # Where the descriptions text files are uploaded.
    descdir = '/home/{}/supplier-data/descriptions/'.format(usernam)
    
    catalog(url,descdir)
    

#------------------------------------------------END OF CODE------------------------------------------------#
