#Dictionary Comprehension
# new_dict = {key: value for key, value in iterable}

#Create a dictionary of squares.
squares = {x: x**2 for x in range(1, 6)}
# print("Squares: ", squares)

#Create a dictionary of cubes
cubes = {x: x**3 for x in range(1, 11)}
# print("Cubes: ", cubes)

#Filter even values from a dictionary
original = {"a": 1, "b": 2, "c": 3, "d": 4}
filtered = {key: value for key, value in original.items() if value % 2 == 0}
"""
Above code is similar to the code below:

filtered = {}
for key, value in original.items():
    if value % 2 == 0:
        filtered[key] = value
"""
# print("Filtered: ", filtered)

"""MERGING DICTIONARIES"""

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

#Using update() method
dict1.update(dict2) #Merges second dictionary to the first one and changes it permanently.
# print(dict1)

#Using | Operator
merged = dict1 | dict2 #Merges second dict to the first returning a new value.
# print("Merged: ", merged)

"""NESTED DICTIONARIES"""

students = {
    "101": {"name": "Alice", "grades": [85, 90, 88]},
    "102": {"name": "Bob", "grades": [78, 82, 84]}
}

#Accessing Data
# print(students["101"]["name"])
# print(students["102"]["grades"][1])

"""SORTING AND FILTERING"""

#Sort dictionary by keys
data = {"b": 3, "a": 1, "c": 2}
sorted_by_keys = dict(sorted(data.items()))
# print(sorted_by_keys)

#Sort dictionary by values
sorted_by_values = dict(sorted(data.items(), key = lambda item: item[1]))
# print(sorted_by_values)
# print(sorted(data.items()))

#Filter dictionary for values greater than 2
filtered_dict = {k: v for k, v in data.items() if v > 2}
# print(filtered_dict)

"""Advanced Dictionary Methods"""
"""
SET DEFAULT: setdefault() method to set a default value for a key if it doesn't exist.
"""
person = {"name": "Alice"}
person.setdefault("age", 25)
# print(person)

"""FROM KEYS: fromkeys() method creates a dictionary from a list of keys with the same value."""
keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys, 0)
# print(default_dict)