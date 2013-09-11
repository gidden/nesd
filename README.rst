This repository is used to house utilities and documents used by my time at
NESD.

Emailing Large Groups of Important People
-----------------------------------------

I had to email long lists of advisors and most had titles (i.e., Dr.). 

Usage
=====

An example python script to be used for this process is provided in
example.py. First adapt it to be used for your email address and password and
test out the automation using the provided email template and test.csv
file. Once you're happy that it works for you, go ahead and export the NESD list
of ANS advisors from our Google Drive in CSV format. Note that it assumes your
advisor names have a prefix (Dr., Mr., Ms., etc.) and that last names are one
word if compounded (e.g. Dr. Mary Johnson-Smith rather than Dr. Mary Johnson
Smith). It should be ready to go once you replace that filename in the example
script!

Final Report
------------

I didn't want to deal with formatting in Word or Google Docs, so I wrote the
final report in Latex. I've included a Make file, so after you grab the files,
you should be able to construct the pdf by simply typing ```make``` on the
command line. Feel free to visit [CTAN](http://www.ctan.org/) if you're missing
any of the required packages.

