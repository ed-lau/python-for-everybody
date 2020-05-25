Question 1
Given the architecture and terminology we introduced in Chapter 1, where are files stored?
Motherboard
Central Processor
Machine Language
Secondary memory

Answer: Secondary memory

Question 2
What is stored in a "file handle" that is returned from a successful open() call?
The handle has a list of all of the files in a particular folder on the hard drive
The handle is a connection to the file's data
The handle contains the first 10 lines of a file
All the data from the file is read into memory and stored in the handle

Answer: The handle is a connection to the file's data

Question 3
What do we use the second parameter of the open() call to indicate?
How large we expect the file to be
The list of folders to be searched to find the file we want to open
Whether we want to read data from the file or write data to the file
What disk drive the file is stored on

Answer: Whether we want to read data from the file or write data to the file

Question 4
What Python function would you use if you wanted to prompt the user for a file name to open?
file_input()
read()
input()
cin

Answer: input()

Question 5
What is the purpose of the newline character in text files?
It adds a new network connection to retrieve files from the network
It indicates the end of one line of text and the beginning of another line of text
It enables random movement throughout the file
It allows us to open more than one files and read them in a synchronized manner

Answer: It indicates the end of one line of text and the beginning of another line of text

Question 6
If we open a file as follows:
xfile = open('mbox.txt')
What statement would we use to read the file one line at a time?

for line in xfile:
while ( getline (xfile,line) ) {
READ xfile INTO LINE
READ (xfile,*,END=10) line
                
Answer: for line in xfile

Question 7
What is the purpose of the following Python code?
fhand = open('mbox.txt')
x = 0
for line in fhand:
        x = x + 1
print x
Count the lines in the file 'mbox.txt'
Reverse the order of the lines in mbox.txt
Remove the leading and trailing spaces from each line in mbox.txt
Convert the lines in mbox.txt to upper case

Answer: Count the lines in the file 'mbox.txt'

Question 8
If you write a Python program to read a text file and you see extra blank lines in the output that are not present in the file input as shown below, what Python string function will likely solve the problem?
From: stephen.marquard@uct.ac.za

From: louis@media.berkeley.edu

From: zqian@umich.edu

From: rjlowe@iupui.edu
...
find()
startswith()
rstrip()
split()
Answer: rstrip()

Question 9
The following code sequence fails with a traceback when the user enters a file that does not exist. How would you avoid the traceback and make it so you could print out your own error message when a bad file name was entered?
fname = raw_input('Enter the file name: ')
fhand = open(fname)
try / except
signal handlers
try / catch / finally
on error resume next

Answer: try/ except

Question 10
What does the following Python code do?
fhand = open('mbox-short.txt')
inp = fhand.read()
Checks to see if the file exists and can be written
Turns the text in the file into a graphic image like a PNG or JPG
Reads the entire file into the variable inp as a string
Prompts the user for a file name

Answer: Reads the entire file into the variable inp as a string


