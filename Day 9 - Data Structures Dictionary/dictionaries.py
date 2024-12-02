"""
Dictionaries: Unordered, mutable and indexed collection in Python.
"""

#Empty Dictionary
empty_dict = {}

#Dictionary with Data
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "hobbies": ['reading', 'traveling']
}

print(person)

#Accessing Dictionary Values via corresponding keys
print(person['name'])

#Accessing Dictionary Values via .get() method. Avoids errors.
print(person.get('name'))

#person['profession'] - This gives a Key Error.
print(person.get('profession')) #This gives None.
print(person.get('profession', 'Key Does Not Exist')) #This gives the second parameter.

#Adding and Updating
person["profession"] = "Software Engineer"  # Add new key-value pair
person["age"] = 26  # Update existing key-value pair


#Removing Key-Value Pair
del person['city'] #Removes the Key-Value Pair.
profession = person.pop('profession') #Removes the Key and returns the value.


#Dictionary Methods
# person.clear() #Empties the dictionary.
print(person)

for key, values in person.items():
    print("Key", key)
    print("Value", values)

#Counting Occurences
text = 'Hello World'
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1

print(char_count)