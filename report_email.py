#!/usr/bin/env python3

# Script-name:  report_email.py

# EDEN: This script will process the supplier fruit descrition data from supplier-data/descriptions directory
# This will also utilize functions from the 'run.py' and 'reports.py'


#--------------------------------------------START OF CODE---------------------------------------------#

import datetime
import os

# Calls the catalog function from the 'run.py' script.
from run import catalog
# Calls the generate_report function from the 'reports.py' script.
from reports import generate_report
# Calls the generate_email and send_email function from the 'emails.py' script.
from emails import generate_email, send_email


# Returns a summary: output and the weight
def gen_pdf(file_format, desc_dir):
    """Returns a summary: output and the weight"""
    
    fin_name = []
    fin_weight = []
    fin_list = ""
    
    # Iterates over the descriptions .txt files
    for file in os.listdir(desc_dir):
        filename = os.path.join(desc_dir,file)
        
        # Opens the file, gets the fruit name and weight, and then assign them to variables.
        with open(filename) as f:
            line = f.readlines()
            weight = line[1].strip('\n')
            name = line[0].strip('\n')
            print(name,weight)
            
            # Adds the fruit name and weight to the separate list.
            fin_name.append('name: ' + name)
            fin_weight.append('weight: ' + weight)

            
    # Checks both list for the fruit-name and weight.
    for i in range(len(fin_name)):
        fin_list += fin_name[i] + "<br />" + fin_weight[i] + "<br />" + "<br />"
            
    return fin_list


if __name__ == "__main__":
    
    usernam = os.getenv('USER')
    
    # Directory containing hte descriptions .txt file
    desc_dir = '/home/{}/supplier-data/descriptions/'.format(usernam)     
    # Format date - DD-MM-YY
    date_now = datetime.date.today().strftime("%d-%B-%Y")   
    # Title of the PDF, alogn with today's date
    title = 'Processed Update on ' + str(date_now)    
    # Calls the generate_report function from the 'reports.py' script  
    generate_report('/tmp/processed.pdf', title, gen_pdf('pdf', desc_dir))  
    
    # EMAIL FORMAT
    subject = 'Upload Completed - Online Fruit Store'  
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    sender = "automation@example.com"
    receiver = "{}@example.com".format(usernam)
    
    # Calls the generate_email function from 'emails.py'
    msg = generate_email(sender,
                         receiver,
                         subject, 
                         body, 
                         "/tmp/processed.pdf")  
    
    # Calls the send_email function from the 'emails.py'
    send_email(msg)
    

#------------------------------------------------END OF CODE------------------------------------------------#
