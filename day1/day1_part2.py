#!/usr/bin/env python

# Opening file to read from
f = open('day1_input.txt', 'r+')

# declare and initialize list with input data
input_list = []
for line in f.readlines():
    input_list.append(int(line))

unique = dict()
current_frequency = 0
unique[current_frequency] = True

list_index = 0
while True:
    # overview
    print "Current frequency %d, change of %d; resulting frequency %d." \
        % (current_frequency, input_list[list_index], current_frequency + input_list[list_index])
    # adding up those frequencies
    current_frequency += input_list[list_index]
    # have we seen this ^ frequency already?
    if unique.has_key(current_frequency):
        # if so we're done here
        print "Found the frequency %d twice" % current_frequency
        break
    # if not let's save the frequence
    unique[current_frequency] = True
    # let's put our currently used index value at the end of our input list to make it easier to loop over it in one 'endless' loop
    input_list.append(input_list[list_index])
    # neeeeeeext
    list_index += 1    
# Closing file pointer
f.close()
