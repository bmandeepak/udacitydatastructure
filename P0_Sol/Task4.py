"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
outgoing_calls = []
for row in calls:
	outgoing_calls.append(row[1].replace(' ',''))

incoming_sms = []
outgoing_sms = []
for row in calls:
	outgoing_sms.append(row[0].replace(' ',''))
	incoming_sms.append(row[1].replace(' ',''))

outgoing_calls_unique = list(set(outgoing_calls))
outgoing_sms_unique = list(set(outgoing_sms))
incoming_sms_unique = list(set(incoming_sms))
telemarketers = []
for row in calls:
	incoming_call = row[0].replace(' ','')
	if incoming_call not in outgoing_calls_unique or incoming_call not in outgoing_calls_unique or incoming_call not in incoming_sms_unique:
		telemarketers.append(incoming_call)

telemarketers_unique = sorted(list(set(telemarketers)))
print('These numbers could be telemarketers:')
for item in telemarketers_unique:
	print(item)

