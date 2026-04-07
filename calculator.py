# Simple Calculator in Python

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error! Division by zero"
    return a / b
print("Simple Calculator")
print("Add")
print("Subtract")
print("Multiply")
print("Divide")
while True:
    choice = input("\nEnter choice (Add/Subtract/Multiple/Divide) or 'q' to quit: ")
    if choice == 'q':
        print("Calculator Closed")
        break
    if choice in ('Add', 'Subtract', 'Multiple', 'Divide'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == 'Add':
            print("Result:", add(num1, num2))
        elif choice == 'Subtract':
            print("Result:", subtract(num1, num2))
        elif choice == 'Multiple':
            print("Result:", multiply(num1, num2))
        elif choice == 'Divide':
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input")