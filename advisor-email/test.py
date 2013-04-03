#! /usr/bin/python

from read_csv import get_advisors

file_handle = 'test.csv'
offset = 1
col_name = 1
col_email = 2

advisors = get_advisors(file_handle,offset,col_name,col_email)
for advisor in advisors:
    print advisor.nice_str()

