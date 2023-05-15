"""
The most popular methods in Python Lists
"""


# Append() Method
# To add new objects into list
simple_list = [1, "2", 3.0, 5, 6.0, "7", 8]
additional_list = ["This", "is", "a", "simple", "list"]
simple_list.append(additional_list)
print(simple_list)

# Insert() Method
# For the addition of elements at the desired position, 
# insert() method is used. 
# Unlike append() which takes only one argument, 
# the insert() method requires two arguments(position, value).
list = [1,2,3,4]
print("Initial List: ")
print(list)
list.insert(3, 12)
list.insert(0, 8)
print(list)
# You can use extend() method to add 3 or more elemets to a list

# Remove() method
# Elements can be removed from the List by using 
# the built-in remove() function but an Error arises 
# if the element doesn’t exist in the list. 
# Remove() method only removes one element at a time, 
# to remove a range of elements, the iterator is used. 
# The remove() method removes the specified item.
list.remove(1)
list.remove(3)
print(list)

# More methods https://www.geeksforgeeks.org/python-lists/