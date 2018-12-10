#!/usr/bin/env python

from collections import Counter

# Opening file to read from
f = open('day2_input.txt', 'r+')

# declare and initialize list with input data
box_IDs = []
for line in f.readlines():
	# removing '\n' from every line
    line = line.rstrip('\n')
    box_IDs.append(line)

exactly_two_of_any_letter = {}
exactly_two_of_any_letter_count = 0
exactly_three_of_any_letter = {}
exactly_three_of_any_letter_count = 0

index_list = 0
for box_ID in box_IDs:
	counter = Counter(box_ID)
	# ^ contains data like this: Counter({'m': 2, 'l': 2, 'p': 2, 'a': 1, 'c': 1, 'e': 1, 'd': 1, ...})
	exactly_two_of_any_letter = dict((k, v) for k, v in counter.items() if v == 2)
	# ^ filtered down to {'p': 2, 'm': 2, 'l': 2}, 246 box IDs have exactly_two_of_any_letter 
	if len(exactly_two_of_any_letter) > 0:
		exactly_two_of_any_letter_count += 1
	exactly_three_of_any_letter = dict((k, v) for k, v in counter.items() if v == 3)
	# ^ contains a lot of {} but also a few like {'d': 3}, 33 box IDs have exactly_three_of_any_letter
	if len(exactly_three_of_any_letter) > 0:
		exactly_three_of_any_letter_count += 1
	index_list += 1

print "Exactly two of any letter: %d" % exactly_two_of_any_letter_count
print "Exactly three of any letter: %d" % exactly_three_of_any_letter_count
print "Checksum: %d " % (exactly_two_of_any_letter_count * exactly_three_of_any_letter_count)
