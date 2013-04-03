#! /usr/bin/python

import smtplib
import csv

class Advisor:

    def __init__(self,name,email):
        self.full_name = name
        self.email = email
        self.title = name.split(' ')[0]
        self.last_name = name.split(' ')[-1]

    def __str__(self):
        return self.name + ", " + self.email

    def nice_str(self):
        return self.title + " " + self.last_name

def get_advisors(file_handle,offset,col_name,col_email):
    advisors = []
    with open(file_handle, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        i = 1
        for row in reader:
            name, email = row[col_name], row[col_email]
            if i > offset and name and email:
                advisors.append(Advisor(name,email))
            i += 1
    return advisors

def get_email_template(template_file,to_replace):
    fp = open(template_file, 'rb')
    text = replace_all(fp.read(),to_replace)
    fp.close()
    return text

def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

def send_advisor_emails(me,pw,msgs,mask=''):
    """ sends a set of gmail email messages """
    # me = your email
    # pw = your pw
    # msgs = a list of MIMEText messages from email.mime.text
    # mask = (optional) a mask you'd prefer to use (e.g. me@uni.edu)

    if not mask:
        mask = me

    # send it as gmail
    server = smtplib.SMTP('smtp.gmail.com',587) #port 465 or 587
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(me,pw)
    for msg in msgs:
        server.sendmail(mask,msg['To'],msg.as_string())
    server.close()

if __name__ == '__main__':
    template_file = 'template'
    name = 'Matthew Gidden'
    title = 'Chair'
    year = '2013'
    to_replace = {'my-name':name,'a-position':title,'a-year':year}

    specialized_template = get_email_template(template_file,to_replace)
    
    print specialized_template
