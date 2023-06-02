"""
Theory about Python Dict
"""


# Dictionary in Python is a collection of keys values, 
# used to store data values like a map, which, 
# unlike other data types which hold only a single value as an element.

# Dict example
person = {
    "age": "23",
    "name": "Antonio",
    "place": "Kazakhstan"
}


# Dict with integer keys
catalog = {
    1: "First",
    2: "Second",
    3: "Third"
}


# Dict with mixed keys
mixed_catalog = {
    1: "First",
    "Second": [1, 2, 3],
    (1,2,): "First, Second"
}


# Dict empty
empty = {"Empty Dict: "}


# Dict creation with method 'dict'
not_empty = dict({"Cat": "Fluffy", "Dog": "Bonny", "Carrot": "Max"})
print(not_empty)


# Dict nested
nested_dict = {
    "Name": "Antonio",
    "Second name": "Kolosov",
    "Hobbies": {"Sport": "Myai Thai",
                "Music": "Jazz",
                "Travel": "Wild Trips"
            }
}


# Adding elements
added_dict = {}
print(added_dict)
added_dict[0] = "Cat"
added_dict[1] = "Dog"
added_dict[2] = "Bird"
print(added_dict)


# Adding set of values
added_dict["Cat"] = "Jack", "Cage", "Tom"
print(added_dict)


# Adding Nested Key value to Dictionary
added_dict["Dog"] = {"Color": {"Fluffy": "Black", "Alex": "White"}}
print(added_dict)


# Accessing a element using key
print(added_dict["Cat"])


# Delete a element using 'del'
del(added_dict["Dog"])
print(added_dict)