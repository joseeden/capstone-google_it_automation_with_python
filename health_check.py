#!/usr/bin/env python3

# Script-name:  health_checkk.py

# EDEN: This script will run in the background monitoring some of the system statistics: 
# CPU usage, disk space, available memory and name resolution. 
# Moreover, this Python script should send an email if there are problems, such as:
#
#    Report an error if CPU usage is over 80%
#    Report an error if available disk space is lower than 20%
#    Report an error if available memory is less than 500MB
#    Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
#
# In the event of any issues detected among the ones mentioned above, an email should be sent.
# Note that the subject line will vary depending on the issue detected:
#
#        if CPU usage is over 80%                           "Error - CPU usage is over 80%"
#
#        if Available disk space is lower than 20%          "Error - Available disk space is less than 20%"
#
#        if available memory is less than 500MB             "Error - Available memory is less than 500MB"
#
#        if hostname "localhost" cannot be resolved         "Error - localhost cannot be resolved to 127.0.0.1"
#        to "127.0.0.1"
#
#   E-mail Body: Please checkk your system and resolve the issue as soon as possible.


#--------------------------------------------START OF CODE---------------------------------------------#

import socket, shutil, psutil, os
import emails

usernam = os.getenv('USER')

# There are 4 checks to be done on the system:
#       chk_cpu -   Checks cpu usage
#       chk_du  -   Checks the disk usage
#       chk_mu  -   Checks the memory usage
#       chk_127 -   Checks if localhost resolves to 127.0.0.1
#
# No alerts will be triggered as long as the checks return TRUE.
# Alert/s will be raised when any or all of the checks return FALSE.


def chk_cpu():
    """Checks cpu usage"""
    
    # this should always return TRUE as long as CPU usage is below 80%
    usage = psutil.cpu_percent(1)
    return usage < 80


def chk_du(disk):
    """Checks the disk usage"""
    
    # This should always return TRUE as long as available disk space is above 20%
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100     
    return free > 20


def chk_mu():
    """Checks the memory usage"""
    
    # This shoudl always return TRUE as long as available memory is above 500MB
    mu = psutil.virtual_memory().available
    total = mu / (1024.0 ** 2)
    return total > 500


def chk_127():
    """Checks if localhost resolves to 127.0.0.1"""
    
    # This should always return TRUE if localhost resolves to 127.0.0.1
    local_host = socket.gethostbyname('localhost')
    return local_host == "127.0.0.1"


# Sends the email if an alert is raised.
# Note that there is no attachment file here. The checking for the attachment path is done
# in the 'emails.py' script.

sender = "automation@example.com"
receiver = "{}@example.com".format(usernam)
body = "Please chk your system and resolve the issue as soon as possible."
attach_path = ""

def send_one(subject):
    email = emails.generate_email(sender,
                                  receiver,
                                  subject,
                                  body,
                                  attach_path)  
    emails.send_email(email)
    

# This section specifies the subject line if an issue detected.
# Note that an issue is detected when any or all of the checks above will return a FALSE.
# The send_one is invoked when an alert/s is raised, which will then send an email.
# Note that the send_one function calls a send_email function from ane external module - 'emails.py'

if not chk_cpu() :
    subject = "Error - CPU usage is over 80%"
    print(subject)
    send_one(subject)

if not chk_du('/') :
    subject = "Error - Available disk space is less than 20%"
    print(subject)
    send_one(subject)
    
if not chk_mu():
    subject = "Error - Available memory is less than 500MB"
    print(subject)
    send_one(subject)

if not chk_127():
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    print(subject)
    send_one(subject)


#------------------------------------------------END OF CODE------------------------------------------------#
