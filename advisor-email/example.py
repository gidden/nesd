#! /usr/bin/python

from email.mime.text import MIMEText
from nesd_email import get_email_template, send_advisor_emails, get_advisors

# get the specialized template
template_file = 'template'
name = 'Matthew Gidden'
title = 'Chair'
year = '2013'
to_replace = {'my-name':name,'a-position':title,'a-year':year}
specialized_template = get_email_template(template_file,to_replace)

# get the list of advisors
file_handle = 'test.csv' # replace once you've tested your automation
offset = 1
col_name = 1
col_email = 2
advisors = get_advisors(file_handle,offset,col_name,col_email)

# for each advisor, populate an email message
msgs = []
me = 'matthew.gidden@gmail.com'
# optional, I prefer for it to look like I'm sending from my school email
mask = 'gidden@wisc.edu' 
for advisor in advisors:
    msg = \
        MIMEText(specialized_template.replace('so-and-so',advisor.nice_str()))
    msg['Subject'] = 'Nuclear Engineering Student Delegation'
    msg['From'] = mask
    msg['To'] = advisor.email
    msgs.append(msg)

# send the messages
pw = 'your-pw' # change this to whatever your password is
send_advisor_emails(me,pw,msgs,mask)
