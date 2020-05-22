__author__ = 'edwardlau'
"""
10.2 Write a program to read through the mbox-short.txt and
figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time
and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts,
sorted by hour as shown below. Note that the autograder
does not have support for the sorted() function.
"""



name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hcount = dict()                                     #create empty dictionary
hlst = []                                           #create empty list

for line in handle: 
    words = line.split()
    if len(words) > 2 and words[0] == 'From':       #Select lines with 'From'
        hr = words[5].split(':')                    #Select hour (5th index) and split string with colon
        hcount[hr[0]] = hcount.get(hr[0], 0) + 1    #increase count for each hour
    else:
        continue

for k,v in hcount.items():                           #k = hour, v = count
    hlst.append((k,v))                               #append tuples to list

hlst.sort()                                         #sort list by hour
for k,v in hlst:                                    #loop through list of tuples
    print k,v                                       #print counts sorted by hour
