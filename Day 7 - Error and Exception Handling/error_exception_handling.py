#Learning how to handle errors and exceptions. 
"""
First let's define errors and exceptions:
Error: A problem that arrises during program execution and stops the execution.
Exception: An error detected during execution that can be handled to prevent program termination.
"""

"""
TYPES OF ERROR

Syntax Error: Incorrect syntax in the code. Eg: Missing something from the syntax.

Type Error: Inompatible data types. Eg: Trying to add String and Integer.

Value Error: Wrong value for an operation. Eg: Passing string into int() function.

Zero Division Error: Division by Zero.
"""

"""
EXCEPTION HANDLING:

Try and except: The "try" block lets you test a block of code for exceptions. The "except" block handles the exception. 
"""

try:
    result = 10/0
except ZeroDivisionError:
    print("Oops! You can't divide by zero.")

"""
Using else and finally: The "else" block executes if no exceptions occur. The "finally" block executes regardless of whether an exception occurs or not.
"""
try:
    num = int(input("Enter a number: "))
    result = 10/num
except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("Invalid input. Please enter an Integer")
else:
    print(f"Result: {result}")
finally:
    print("Execution complete")

"""
Using Raise: "raise" is used to explicityly trigger an exception with the message.
"""
age = -5
if age < 0:
    raise ValueError("Age cannot be negative")