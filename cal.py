print("Welcome to Simple Scientific Calculator")

# Functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def power(x, y):
    result = 1
    for _ in range(int(y)):
        result = result * x
    return result

def square_root(x):
    if x < 0:
        return "Error: Negative number"
    guess = x / 2
    for _ in range(20):
        guess = (guess + x / guess) / 2
    return guess


# Display operations
print("\nSelect operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power")
print("6. Square Root")

choice = input("Enter choice (1-6): ")

# Based on choice
if choice in ['1', '2', '3', '4', '5']:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    elif choice == '5':
        print("Result:", power(num1, num2))

elif choice in ['6']:
    num = float(input("Enter number (angle in degrees for trigonometry): "))

    if choice == '6':
        print("Result:", square_root(num))

else:
    print("Invalid choice. Please run the program again.")