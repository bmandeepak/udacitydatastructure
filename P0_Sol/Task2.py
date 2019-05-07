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
total_time = {}
for row in calls:
	outgoing_telephone_no = row[0]
	incoming_telephone_no = row[1]
	
	date_time_str = row[2]
	date_time_obj = datetime.datetime.strptime(date_time_str, '%d-%m-%Y %H:%M:%S')
	month = datetime.date(1900, date_time_obj.month, 1).strftime('%B')
	year = date_time_obj.year
	time_sec  = int(row[3])
	if outgoing_telephone_no not in total_time.keys():
		total_time[outgoing_telephone_no] = time_sec
	else:
		total_current_time = total_time[outgoing_telephone_no]
		total_current_time += time_sec
		total_time[outgoing_telephone_no] = total_current_time

	if incoming_telephone_no not in total_time.keys():
		total_time[incoming_telephone_no] = time_sec
	else:
		total_current_time = total_time[incoming_telephone_no]
		total_current_time += time_sec
		total_time[incoming_telephone_no] = total_current_time

sorted_total_time = sorted(total_time.items(), key=lambda x: x[1],reverse=True)

print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(sorted_total_time[0][0],sorted_total_time[0][1]))