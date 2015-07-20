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
text = open(name)

hours = dict()

for line in text:
    line.rstrip()
    if not line.startswith("From "): continue
    words = line.split()

    hour = words[5].split(":")
    hours[hour[0]] = hours.get(hour[0],0) + 1

lst = []

for a,b in hours.items():
    lst.append((a,b))

lst.sort()


for a,b in lst:
    print a,b