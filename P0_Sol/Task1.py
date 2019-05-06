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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
unique_phone = []
for row in texts:
	incoming_number = row[0]
	if incoming_number.find(' ')!=-1:
		incoming_number.replace(' ','')
	answering_number  = row[1]
	if answering_number.find(' ')!=-1:
		answering_number.replace(' ','')
	if incoming_number not in unique_phone:
		unique_phone.append(incoming_number)
	if answering_number not in unique_phone:
		unique_phone.append(answering_number)


for row in calls:
	incoming_number = row[0]
	if incoming_number.find(' ')!=-1:
		incoming_number.replace(' ','')
	answering_number  = row[1]
	if answering_number.find(' ')!=-1:
		answering_number.replace(' ','')
	if incoming_number not in unique_phone:
		unique_phone.append(incoming_number)
	if answering_number not in unique_phone:
		unique_phone.append(answering_number)
print('There are {} different telephone numbers in the records'.format(len(unique_phone)))