#! /usr/bin/python

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

if __name__ == '__main__':
    
    file_handle = 'test.csv'
    offset = 1
    col_name = 1
    col_email = 2

    advisors = get_advisors(file_handle,offset,col_name,col_email)
    for advisor in advisors:
        print advisor.nice_str()
