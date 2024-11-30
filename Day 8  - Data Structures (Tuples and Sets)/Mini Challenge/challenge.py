"""
MINI CHALLENGE

Create a tuple containing the names of 5 cities. Write a program to:

Print the second and last city.
Concatenate another tuple containing 2 more cities.
Create a set of numbers from 1 to 10. Write a program to:

Remove all even numbers from the set.
Add the numbers 11 and 12 to the set.
Find the union of the updated set with {15, 16, 17}.


"""

#Tuple of cities
cities = ("Kathmandu", "New York", "London", "Toronto", "Sydney")

#Printing second and last city
print("Second City: ", cities[1])
print("Last City: ", cities[-1])

more_cities = ("Auckland", "New Delhi")
final_cities = cities + more_cities

print("Final City List: ", final_cities)


#Set of Numbers from 1-10
nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
final_num = set()
#Removing even numbers
for i in range(0, len(nums)):
    nums_list = list(nums)

    if nums_list[i] % 2 == 0:
        nums_list.remove(nums_list[i])
        continue

    final_num.add(nums_list[i])

print("Nums without Even Numbers: ", final_num)

final_num.add(11)
final_num.add(12)

print("Final Number Set: ", final_num)

union_set = final_num | {15, 16, 17}

print("Union of Set: ", union_set)