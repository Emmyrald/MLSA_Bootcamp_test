# Create a function that erforms basic arithmetic operations based on user's input
def arithmetic ():
    operation = input ('''
                        what would you like to do?
                        Add (+),
                        Subtract (-),
                        Multiply (X),
                        Divide (/)
                        ''').lower().strip()
    num_1 = float (input("Enter the first number: "))
    num_2 = float (input(f"Enter the number to {operation} with: "))
    if operation == "add" or operation == "+":
        Result = num_1 + num_2
    elif operation == "subtract" or operation == "-":
        Result = num_1 - num_2
    elif operation == "multiply" or operation == "*":
        Result = num_1 * num_2
    elif operation == "divide" or operation == "/":
        Result = num_1 / num_2
    else:
        Result = "Your input doesn't match the options"
    return Result
    
print (arithmetic ())