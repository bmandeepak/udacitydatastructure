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
call_record = []
telemarketers = []

incoming_calls = []

for row in calls:
	incoming_calls.append(row[1].replace(' ',''))

incoming_calls_unique = list(set(incoming_calls))

for row in texts:
	call_record.append(row[0].replace(' ',''))
	call_record.append(row[1].replace(' ',''))

call_record_unique = list(set(call_record))

for row in calls:
	outgoing_call = row[0].replace(' ','')
	if outgoing_call not in call_record_unique or outgoing_call not in incoming_calls_unique: 
		telemarketers.append(outgoing_call)

telemarketers_unique = sorted(list(set(telemarketers)))
print('These numbers could be telemarketers:')
for item in telemarketers_unique:
	print(item)

