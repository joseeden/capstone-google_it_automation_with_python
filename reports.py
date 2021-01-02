#!/usr/bin/env python3

# Script-name:  reports.py

# EDEN: This script generates the PDF file to be sent to the supplier,
# which will then that indicate that the data was correctly processed.


#--------------------------------------------START OF CODE---------------------------------------------#


# Followed the same procedures that was discussed in the lecture videos of the course.
from reportlab.platypus import Paragraph, Spacer, Image, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet

# This formats how the report will look like
# This function will be called by another program, 'report_email.py'
def generate_report(file, title, details):
    """This formats how the report will look like"""
    
    style = getSampleStyleSheet()
    report = SimpleDocTemplate(file)
    rep_title = Paragraph(title, style['h1'])
    rep_info = Paragraph(details, style['BodyText'])
    blank_line = Spacer(1,20)

    # Generates the report.
    report.build([rep_title, 
                  blank_line, 
                  rep_info, 
                  blank_line])


#------------------------------------------------END OF CODE------------------------------------------------#
