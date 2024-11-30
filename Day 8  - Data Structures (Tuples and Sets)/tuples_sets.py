"""
Tuples: An ordered, immutable collection of items. Once created, cannot be modified,
add or remove elements from tuple.
Defined using parenthesis ().
"""


#Creating Tuples

#Empty Typle
empty_tuple = ()

#Tuple with elements
fruit_tuple = ("apple", "banana", "cherry")

#Acessing Elements
print(fruit_tuple[0])
print(fruit_tuple[-1])

"""
Sets: An unordered, mutable collection of unique items. Defined using curly braces {}.
"""

#Empty Sets
empty_sets = set()

#Set with elements
num_set = {1, 2, 3, 4, 5}

#Set with duplicates
duplicate_set = {1, 2, 2, 3}
print('Duplicate Set', duplicate_set)

#Adding and removing elements
num_set.add(6)
num_set.remove(3)

#Membershipt testing
print(4 in num_set)
print(3 not in num_set)

#Length of a set
print(len(num_set))

#Mathematical Operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

#Union: Combines both values.
print("Union: ", set_a | set_b)

#Intersection: Finds the common ones only.
print("Intersection: ", set_a & set_b)

#Difference: Removes the common ones and only shows the remaining elements from the first set.
print("Difference: ", set_a - set_b)

#Symmetric Difference: Removes the common ones and shows the remaning from both.
print("Symmetric Diff.: ", set_a ^ set_b)