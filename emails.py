#!/usr/bin/env python3

# Script-name:  emails.py

# EDEN: This script contains the generate_email and send_email function which will be utilized by the 
# report_email.py script


#--------------------------------------------START OF CODE---------------------------------------------#

import email
import mimetypes
import smtplib
import os

# Generates the email
def generate_email(sender, receiver, subject, body, attach_path):
    
    # Formats the email based on the parameters
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject
    message.set_content(body)

    # Isolated attachment path. 
    # Since it's required to have this, the email won't be sent if the attachment path is blank.
    # Otherwise, add attachment to email.
    if attach_path != "":
        
        attach_file = os.path.basename(attach_path)
        mime_type, _ = mimetypes.guess_type(attach_path)
        mime_type, mime_subtype = mime_type.split('/', 1)

        with open(attach_path, 'rb') as ap:
            message.add_attachment(ap.read(), 
                                   maintype = mime_type, 
                                   subtype = mime_subtype,
                                   filename = attach_file)

    return message


# Sends the email to the configured SMTP server
def send_email(message):
    
    mail_svr = smtplib.SMTP('localhost')
    mail_svr.send_message(message)
    mail_svr.quit()


#------------------------------------------------END OF CODE------------------------------------------------#
