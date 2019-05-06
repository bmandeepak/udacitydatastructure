"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

codes  = []
for row in calls:
	incoming_no = row[0].replace(' ','')
	if re.search('^\(080\)', incoming_no):
		answering_no = row[1].replace(' ','')
		if answering_no.find('(0')!=-1:
			fixed_line_code = answering_no.split(')')[0]
			codes.append(fixed_line_code[1:])
		if re.search("^140", answering_no):
			codes.append(answering_no[:3])
		if re.search("^7|^8|^9", answering_no):
			codes.append(answering_no[:4])

unique_codes = sorted(list(set(codes)))
print('The numbers called by people in Bangalore have codes:')
for code in unique_codes:
	print(code)


total_calls = 0
to_fixed_lines = 0
for row in calls:
	incoming_no = row[0].replace(' ','')
	if re.search('^\(080\)', incoming_no):
		total_calls+=1
		answering_no = row[1].replace(' ','')
		if re.search('^\(080\)', answering_no):
			to_fixed_lines+=1
percentage_to_fixed = to_fixed_lines/float(total_calls)
print('{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(round(percentage_to_fixed,2)*100))
