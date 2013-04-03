#! /usr/bin/python

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# values to change
template_file = 'template'
name = 'Matthew Gidden'
me = 'matthew.gidden@gmail.com'
password = 'somepw'
advisors = ['advisor1','advisor2']
emails = ['email1@testemail1.com','email2@testemail1.com']

# Open a plain text file for reading.  
fp = open(template_file, 'rb')
# Create a text/plain message
msg = MIMEText(fp.read())
fp.close()

# from == the sender's email address
# to == the recipient's email address
msg['Subject'] = 'Nuclear Engineering Student Delegation'
msg['From'] = me
msg['To'] = emails[0]

# send it as gmail
server = smtplib.SMTP('smtp.gmail.com',587) #port 465 or 587
server.ehlo()
server.starttls()
server.ehlo()
server.login(me,somepw)
server.sendmail(me,emails[0],msg.as_string())
server.close()
