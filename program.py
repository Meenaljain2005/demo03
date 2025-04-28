print("Welcome to Simple Scientific Calculator (No Libraries, No Loops)")

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
    if y == 0:
        return 1
    elif y == 1:
        return x
    elif y == 2:
        return x * x
    elif y == 3:
        return x * x * x
    elif y == 4:
        return x * x * x * x
    else:
        return "Error: Power function supports integer exponents up to 4 without loops"

def square_root(x):
    if x < 0:
        return "Error: Negative number"
    guess = x / 2
    # 20 manual Newton-Raphson steps
    guess = (guess + x / guess) / 2
    guess = (guess + x / guess) / 2
    guess = (guess + x / guess) / 2
    guess = (guess + x / guess) / 2
    guess = (guess + x / guess) / 2
    guess = (guess + x / guess) / 2
    guess = (guess + x / guess) / 2
    guess = (guess + x / guess) / 2
    guess = (guess + x / guess) / 2
    guess = (guess + x / guess) / 2
    guess = (guess + x / guess) / 2
    guess = (guess + x / guess) / 2
    guess = (guess + x / guess) / 2
    guess = (guess + x / guess) / 2
    guess = (guess + x / guess) / 2
    guess = (guess + x / guess) / 2
    guess = (guess + x / guess) / 2
    guess = (guess + x / guess) / 2
    guess = (guess + x / guess) / 2
    guess = (guess + x / guess) / 2
    return guess

# Approximations for sin, cos, tan (x in degrees)

def degrees_to_radians(deg):
    return deg * (3.141592653589793 / 180)

def sin(x):
    x = degrees_to_radians(x)
    return x - (x**3)/6 + (x**5)/120 - (x**7)/5040

def cos(x):
    x = degrees_to_radians(x)
    return 1 - (x**2)/2 + (x**4)/24 - (x**6)/720

def tan(x):
    cos_value = cos(x)
    if cos_value == 0:
        return "Error: tan undefined at 90°, 270°, etc."
    return sin(x) / cos(x)

# Display operations
print("\nSelect operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power (only positive integers up to 4)")
print("6. Square Root")
print("7. Sine (sin)")
print("8. Cosine (cos)")
print("9. Tangent (tan)")

choice = input("Enter choice (1-9): ")

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

elif choice == '6':
    num = float(input("Enter number: "))
    print("Result:", square_root(num))

elif choice == '7':
    num = float(input("Enter angle in degrees: "))
    print("sin(", num, ") =", sin(num))

elif choice == '8':
    num = float(input("Enter angle in degrees: "))
    print("cos(", num, ") =", cos(num))

elif choice == '9':
    num = float(input("Enter angle in degrees: "))
    print("tan(", num, ") =", tan(num))

else:
    print("Invalid choice. Please run the program again.")
