def calculator():
    first_num = int(input("Enter first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    second_num = int(input("Enter second number: "))

    try:
        if(operator == "+"):
            result = first_num + second_num
        elif(operator == "-"):
            result = first_num - second_num
        elif(operator == "*"):
            result = first_num * second_num
        elif(operator == "/"):
            result = first_num / second_num
        else:
            raise ValueError("Unsupported Operator. Please enter one from the options.")

        print(f"The result is: {result}")

    except ZeroDivisionError as zde:
        print("Division by zero is not allowed")
    except ValueError as vle:
        print(f"Error: {vle}")

calculator()