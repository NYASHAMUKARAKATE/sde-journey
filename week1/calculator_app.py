# This code implements a simple calculator app that can perform basic arithmetic operations
# such as addition, subtraction, multiplication, division, power, and square root.
# It includes error handling for division by zero and square root of negative numbers.
# The calculator runs in a loop, allowing users to perform multiple calculations until they choose to exit.
# The user is prompted to select an operation and input numbers, and the result is displayed.

import math

def add(x, y):
    """Return the sum of the numbers x and y."""
    return x + y

def subtract(x, y):
    """Return the difference of x and y."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return the quotient of x and y."""
    if y != 0:
        return x / y
    else:
        return "Division by zero error"

def power(x, y):
    """Return x raised to the power of y."""
    return math.pow(x, y)
def square_root(x):
    """Return the square root of x."""
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Square root of negative number error"
    
def calculator():
    print("---------------Welcome to the Calculator App!--------\n")
    print("--------------------Select operation------------------\n")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("------------------------------------------------------\n")

    while True:
        choice = input("Enter choice (1 / 2 / 3 / 4 / 5 / 6): ")

        if choice in ['1', '2', '3', '4', '5', '6']:
            if choice == '6':
                num = float(input("Enter number you want to find the square root of: "))
                result = square_root(num)
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    result = add(num1, num2)
                elif choice == '2':
                    result = subtract(num1, num2)
                elif choice == '3':
                    result = multiply(num1, num2)
                elif choice == '4':
                    result = divide(num1, num2)
                elif choice == '5':
                    result = power(num1, num2)

            print(f"\nResult : {result}")
        else:
            print("\nInvalid input please try again.")

        next_calculation = input("Do you want to do another calculation? (yes/no) : ")
        if next_calculation.lower() != 'yes':
            break
    print("Thank you for using the Calculator App!")
if __name__ == "__main__":
    calculator()

