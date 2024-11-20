# # Module is a file in Python that contains definition and statements.
# # import math_tools
# # print(math_tools.add(3, 5))

# #Using Import: Import the entire module
# import math
# # print(math.sqrt(25))
# print(dir(math))

# #Using From: Import only the specific function or variable.
# from math import sqrt
# print(sqrt(16))

# #Using as: Import and rename module for convinience
# from math import sqrt as s
# print(s(49))


## CALCULATOR MINI CHALLENGE
import calculator as c
x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))

print(f"Addition: {c.add(x, y)}")
print(f"Subtraction: {c.subtract(x, y)}")
print(f"Multiplication: {c.multiply(x, y)}")
print(f"Division: {c.divide(x, y)}")
