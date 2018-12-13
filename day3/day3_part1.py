#!/usr/bin/env python

import numpy as np

# Opening file to read from
f = open('day3_input.txt', 'r+')

#num_lines = sum(1 for line in f)
#print num_lines
#1265

# declare and initialize list with input data
claims = []
for line in f.readlines():
	# before e.g. '#1265 @ 429,317: 24x28'
	for char in line:
		if char in "#@,:;x\n":
			line =  line.replace(char,' ')
	# -> ' 1265   429 317  24 28'
	line = filter(None, line.split(' '))
	# -> ['1265', '429', '317', '24', '28']
	claims.append(line)
#print claims

fabric = np.zeros((1000,1000),dtype=np.int)

z = 0
while z < len(claims):
	y = 0
	while y + int(claims[z][2]) < (int(claims[z][2]) + int(claims[z][4])):
		#print "y: %d + int(claims[z][2]): %d = %d" % (y, int(claims[z][2]), y + int(claims[z][2])) 
		x = 0
		while x + int(claims[z][1]) < (int(claims[z][1]) + int(claims[z][3])):
			#print "indices filled: [%d][%d]" % (x + int(claims[z][1]), y + int(claims[z][2]))
			fabric[x + int(claims[z][1])][y + int(claims[z][2])] += 1
			x += 1
		y += 1
	z += 1

x = 0
overprovisioned = 0
while x < 1000:
	y = 0
	while y < 1000:
		#print fabric[x][y]
		if fabric[x][y] > 1:
			overprovisioned += 1
		y +=1
	x += 1
print overprovisioned
