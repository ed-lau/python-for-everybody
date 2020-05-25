__author__ = 'edwardlau'


"""
9.4 Write a program to read through the mbox-short.txt and
figure out who has the sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those
lines as the person who sent the mail. The program creates a Python dictionary
that maps the sender's mail address to a count of the number of times they appear in
the file. After the dictionary is produced,
the program reads through the dictionary using a maximum loop to find the most prolific committer.



name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
text = open(name)

maxauthor = dict()

for line in text:
    line.rstrip()
    if not line.startswith("From "): continue
    words = line.split()
    maxauthor[words[1]] = maxauthor.get(words[1],0)+1

largest = None
largest_author = None

for key in maxauthor:
    if largest is None: largest = maxauthor[key]

    if largest < maxauthor[key]:
        largest = maxauthor[key]
        largest_author = key

print(largest_author, largest)
