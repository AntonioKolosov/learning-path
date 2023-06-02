"""
Simple Implementation for Dict
"""

import json

methods = {
    "dic.clear()": "Remove all the elements from the dictionary",
    "dict.copy()": "Returns a copy of the dictionary",
    "dict.get(key, default = “None”)": "Returns the value of specified key",
    "dict.items()": "Returns a list containing a tuple for each key value pair",
    "dict.keys()": " Returns a list containing dictionary's keys",
    "dict.update(dict2)": "Updates dictionary with specified key-value pairs",
    "dict.values()": " Returns a list of all the values of dictionary",
    "pop()": "Remove the element with specified key",
    "popItem()": "Removes the last inserted key-value pair"
}


json_object = json.dumps(methods, indent = 4) 
print(json_object)