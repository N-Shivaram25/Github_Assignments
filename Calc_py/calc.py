import math

def get_input():
    """Function to take input from the user."""
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b

def add(a, b):
    return a + b

def subtract(a, b):
    return a-b    

def multiply(a, b):
    return a*b

def divide(a, b):
    return a//b
    

def square_root(a):
    

def calculator():
    print("\nWelcome to the Mini Calculator!")
    a, b = get_input()
    print(f"\nYou entered: a = {a}, b = {b}")
    print(f"1. Addition: {add(a, b)}")
    print(f"2. Subtraction: {subtract(a,b)}")
     print(f"3. Multpilcation: {multiply(a, b)}")
    print(f"4.division: {divide(a,b)}")
    

if __name__ == "__main__":
    calculator()
