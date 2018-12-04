#!/usr/bin/python

# Open file for reading
f = open('input.txt', 'r+')
result = 0
for line in f.readlines():
    result += int(line) 
f.close()
print result
