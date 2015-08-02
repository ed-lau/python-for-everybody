__author__ = 'edwardlau'
"""
Question 1
What will the following Python program print out:
def fred():
   print "Zap"

def jane():
   print "ABC"

fred()
jane()
fred()
"""
#Answer: Zap ABC Zap

"""
Question 2
What would the following Python code sequence print?
str = "hello there bob"
print str[0]
there
hello there bob
h
It would fail with an index error
"""
#Answer: h

"""
Question 3
What part of a computer is actually doing the addition and subtraction in the following statement:
x = 1 + 2 - 3 * 4 / 5 + 6
Central Processing Unit
Network Controller
Input Devices
Cloud
"""
#Answer: Central Processing Unit

"""
Question 4
Which of the following lines will never print out regardless of the value for x?
if x < 2 :
    print "Below 2"
elif x < 0 :
    print "Negative"
else :
    print "Something else"
All three lines will print all the time
Negative
Something else
Below 2
"""
#Answer: Negative


"""
Question 5
What will the following code print out?
x = 12
if x <= 10:
   if x > 4:
      print "One"
   else:
      print "Two"
else:
   if x >= 11:
      print "Three"
   else:
      print "Four"
One
Three
Two
Four
"""
#Answer: Three

"""
Question 6
What would the following Python print out?
abc = "With three words"
stuff = abc.split()
print len(stuff)
['With three words']
14
16
['With', 'three', 'words']
2
3
6
"""
#Answer: 3


"""
Question 7
What would the value of the following expression be:
abc = 1 + 2 - 3 * 4 + 5 - 6 / 3
36
0.9675
42
-6
"""
#Answer: -6


"""
Question 8
What is the primary use of the Python dictionary?
To make sure that the definitions of the Python reserved words are available in different languages (French, Spanish, etc)
To insure that all Python reserved words are properly spelled
To store key / value pairs
To store items in order (like a can of Pringles potato chips)
"""

#Answer: To store key / value pairs

"""
Question 9
What will the following Python program print out:
def fred():
   print "Zap"

def jane():
   print "ABC"

jane()
fred()
jane()
"""
#Answer: ABC Zap ABC

"""
Question 10
Which of these is not one of the four types of control flow used in programs:
Conditional
Repeated
Store and Reuse
Fused / Multi-Path
"""
Answer: Fused/ Multi-Path


"""
Question 11
What would happen if the following Python code were executed?
st = "abc"
ix  = int(st)
The variable ix would contain 0
The variable ix would contain None
The program would show an error and a traceback on the second line
The variable ix would contain -1
"""

# Answer: The program would show an error and a traceback on the second line

"""
Question 12
What would this code print out?
lst = []
lst.append(4)
lst.append(10)
lst.append(21)
lst.append(6)
print lst[2]
none of the above
21
10
4
"""

#Answer: 21

"""
Question 13
If all of the following were used in a Python expression, which would have the highest precedence (i.e. which would be evaluated first)?
Subtraction
Modulo (i.e. remainder)
Parenthesis
Addition
"""

# Answer: Parenthesis

"""
Question 14
If you want your program to recover from errors that would otherwise cause a trace back and your program to stop, what language element of Python would you use?
try / except
on_error / goto
repeat / on_error
when / error
"""

# Answer: try/except

"""
Question 15
You develop the following program in Python:
f = int(raw_input("Enter:"))
c = ( f - 32 ) * ( 5 / 9 )
print "Celsius",c
And when you run it three times you get the following output:
Enter:212
Celsius 0

Enter:72
Celsius 0

Enter:15
Celsius 0
What part of the program is causing the output to always be zero?
( f - 32 )
Using single character variables
Using double quotes for all the strings
( 5 / 9 )
"""

#Answer: (5/9)

"""
Question 16
For the following Python program, what will it print out?
x = 0
for value in [3, 41, 12, 9, 74, 15] :
    if value < 10 :
        x = x + value
print x
41
12
15
9
"""

#Answer: 12

"""
Question 17
What would the following Python code print out?
fline = "blah blah"

if len(fline) > 1 :
    print "More than one"
    if fline[0] == "h" :
        print "Has an h"
print "All done"
More than one
All done
More than one
Has an h
All done
Has an h
All done
Nothing will print
"""

#Answer: More than one, all done

"""
Question 18
What is the value of the following expression:
abc = 1 - 2 + 3 * 4 - 5 - 6 / 3
4
18
42
0
"""

# Answer: 4

"""
Question 19
What would the following Python code print out?
stx = "hello there bob how are you"
wds = stx.split()
print wds[2]
bob
are
e
how
"""

# Answer: bob

"""
Question 20
For the following Python program, what will it print out?
x = -1
for value in [3, 41, 12, 9, 74, 15] :
    if value < x :
        x = value
print x
21
74
15
-1
"""

# Answer: -1