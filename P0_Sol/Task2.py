"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
import datetime
from datetime import timedelta

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

max_call_time = 0
telephone_no = None
month = None
year = None

# Code Complexity is O(n)
for row in calls:
	telephone_no = row[0]
	date_time_str = row[2]
	date_time_obj = datetime.datetime.strptime(date_time_str, '%d-%m-%Y %H:%M:%S')
	month = datetime.date(1900, date_time_obj.month, 1).strftime('%B')
	year = date_time_obj.year
	time_sec  = int(row[3])
	if max_call_time<time_sec:
		max_call_time = time_sec
		month = month
		telephone_no = telephone_no
print('{} spent the longest time, {} seconds, on the phone during {} {}.'.format(telephone_no,max_call_time,month,year))