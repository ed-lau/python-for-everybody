__author__ = 'edwardlau'
"""
Question 1
How are Python dictionaries different from Python lists?
Python lists are indexed using integers and dictionaries can use strings as indexes
Python dictionaries are a collection and lists are not a collection
Python lists can store strings and dictionaries can only store words
Python lists store multiple values and dictionaries store a single value
"""

# Answer: Python lists are indexed using integers and dictionaries can use strings as indexes

"""
Question 2
What is a term commonly used to describe the Python dictionary feature in other programming languages?
Closures
Sequences
Associative arrays
Lambdas
"""

# Answer: Associative arrays

"""
Question 3
What would the following Python code print out?
"""

stuff = dict()
print stuff['candy']

"""
The program would fail with a traceback
0
-1
candy
"""

# Answer: The program would fail with a traceback

"""
Question 4
What would the following Python code print out?
stuff = dict()
print stuff.get('candy',-1)
The program would fail with a traceback
'candy'
0
-1
"""

# Answer: -1

"""
Question 5
(T/F) When you add items to a dictionary they remain in the order in which you added them.
False
True
"""

# Answer: False

"""
Question 6
What is a common use of Python dictionaries in a program?
Computing an average of a set of numbers
Sorting a list of names into alphabetical order
Building a histogram counting the occurrences of various strings in a file
Splitting a line of input into words using a space as a delimiter
"""

# Answer: Building a histogram counting the occurrences of various strings in a file

"""
Question 7
Which of the following lines of Python is equivalent to the following sequence of statements assuming that counts is a dictionary?
if key in counts:
    counts[key] = counts[key] + 1
else:
    counts[key] = 1
counts[key] = counts.get(key,0) + 1
counts[key] = counts.get(key,-1) + 1
counts[key] = (key in counts) + 1
counts[key] = key + 1
counts[key] = (counts[key] * 1) + 1
"""

# Answer: counts[key] = counts.get(key,0) + 1

"""
Question 8
In the following Python, what does the for loop iterate through?
x = dict()
...
for y in x :
    ...
It loops through the integers in the range from zero through the length of the dictionary
It loops through all of the dictionaries in the program
It loops through the values in the dictionary
It loops through the keys in the dictionary
"""
# Answer: It loops through the keys in the dictionary

"""
Question 9
Which method in a dictionary object gives you a list of the values in the dictionary?
items()
keys()
values()
all()
each()
"""

# Answer: values()

"""
Question 10
What is the purpose of the second parameter of the get() method for Python dictionaries?
An alternate key to use if the first key cannot be found
The value to retrieve
To provide a default value if the key is not found
The key to retrieve
"""

# Answer: To provide a default value if the key is not found


