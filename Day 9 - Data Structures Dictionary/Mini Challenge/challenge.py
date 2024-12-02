"""
MINI CHALLENGE
Create a dictionary to store the names and ages of 5 people. Write a program to:

Add a new entry for another person.
Update the age of one person.
Delete the entry of one person.
Write a program to count the occurrences of each word in a given sentence using a dictionary.
"""

people = {"people": [
    {
        "name": "John Doe",
        "age": 21 
    },
    {
        "name": "Jane Doe",
        "age": 19
    },
    {
        "name": "Jason Marz",
        "age": 54
    },
    {
        "name": "Neville Richard",
        "age": 72
    },
    {
        "name": "Mark Calloway",
        "age": 25
    }
]}

people['people'].append({
    "name": "Randy Orton",
    "age": 54
})

#Updating the age of any one person: Jane Doe
people["people"][1]["age"] = 32

#Deleting the entry of any one person: Jason Marz
del people["people"][2]

#Counting the occurences
sentence = "This is a Dictionary Mini Challenge"
char_occurence = {}

for char in sentence:
    char_occurence[char] = char_occurence.get(char, 0) + 1

print("Character Occurence: ", char_occurence)