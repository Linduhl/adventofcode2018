#!/usr/bin/env python

# Opening file to read from
f = open('input.txt', 'r+')
# Adding up frequencies
result = 0
for line in f.readlines():
    result += int(line)
# Closing that file pointer
f.close()
# What's the result?
print "Resulting frequency: %d" %result
