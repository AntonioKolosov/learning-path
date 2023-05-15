"""
Theory about Python List
"""


# Basic List
# In Python, a list is one of the built-in data types,
# which is an ordered set of values, where each element has its own index. 
# Lists in Python can be created using square brackets [] or the list() function.

# This is a simple list with a same types of data
simple_list = [1, 2, 3, 4, 5]

# This is a list with different types of data
different_list = [1, "two", 3.0]

# To access the list items, indexing is used, which starts from 0.
print (different_list[1]) # -> "two"

# Negative indexing
print (different_list[-2]) # -> "two"

# A list with multiple distinct or duplicate elements
# A list may contain duplicate values with their distinct positions and hence, 
# multiple distinct or duplicate values can be passed 
# as a sequence at the time of list creation.
duplicate_list = [1, 2, 4, 4, 3, 3, 3, 6, 5]

# Getting the size of Python list
print(len(duplicate_list)) # -> 9

# Getting input of Python list
inp = input("Put your words: ")
inp_list = inp.split()
print(inp_list)