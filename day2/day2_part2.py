#!/usr/bin/env python

#import numpy as np
#from future_builtins import zip
import collections


# Opening file to read from
f = open('day2_input.txt', 'r+')

#num_lines = sum(1 for line in f)


# declare and initialize list with input data
box_IDs = []
for line in f.readlines():
	# removing '\n' from every line
    line = line.rstrip('\n')
    box_IDs.append(line)
#print box_IDs

#box_IDs = ['abcde','fghij','klmno','pqrst','fguij','axcye','wvxyz']

# declare a list of counters
cnt_list = list()
# for every box ID
for box_ID in box_IDs:
	# use a separate counter 
	cnt = collections.Counter()
	for char in box_ID:
		# and store what chars and how many of them are in each box_ID
		cnt[char] += 1
	# save this counter in the list 
	cnt_list.append(cnt)
#print cnt_list

# counter variable
x = 0
# for storing which indices of box_IDs are correct 
results = list()
# for each box_ID
while x < len(box_IDs):
	# yet another counter variable
	y = 0
	# compare with every other box_ID 
	while y < len(box_IDs):
		# except with itself
		if x == y:
			y += 1
			continue
		# substract counters 
		if len(cnt_list[x] - cnt_list[y]) == 1 and len(cnt_list[y] - cnt_list[x]) == 1:
			"""
			print box_IDs[x]
			print box_IDs[y]
			print cnt_list[x] - cnt_list[y]
			print cnt_list[y] - cnt_list[x]
			"""
			results.append([box_IDs[x],box_IDs[y]])
		y += 1
	x += 1
#print results

# at thit point I must realise that proper reading of the task is a nice skill to have :D
# I missed that the position in both strings must be the same
# I could find it manually though ...  
# Also adding results twice ... [1,4] == [4,1] ...
# could be solved by using some kind of upper/lower triangular matrix datatype
"""
rbrenqtlagdhixmwyscfukzodp
kbrenqtlagxhirmwyscfupzodp
Counter({'d': 1})
Counter({'p': 1})
jbbenqtlagxhivmwyscjukztdp
jbbenqtlavxhivmwyscjukztdp
Counter({'g': 1})
Counter({'v': 1})
kbrenqtlagxhirmwyscfupzodp
rbrenqtlagdhixmwyscfukzodp
Counter({'p': 1})
Counter({'d': 1})
jbrenqtnarxhivmwyscfmkzodp
jbrenqtlamxhivmwyscfnkzorp
Counter({'d': 1})
Counter({'l': 1})
jbrenqtlamxhivmwyscfnkzorp
jbrenqtnarxhivmwyscfmkzodp
Counter({'l': 1})
Counter({'d': 1})
jbbenqtlavxhivmwyscjukztdp
jbbenqtlagxhivmwyscjukztdp
Counter({'v': 1})
Counter({'g': 1})
[[59, 157], [120, 198], [157, 59], [196, 197], [197, 196], [198, 120]]
"""
# correct answer: jbbenqtlaxhivmwyscjukztdp
