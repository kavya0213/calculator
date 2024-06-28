import math

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed")
    return x / y

# Function to compute square root
def square_root(x):
    if x < 0:
        raise ValueError("Square root of a negative number is not real")
    return math.sqrt(x)

# Function to compute exponentiation
def power(x, y):
    return x ** y

# Main calculator function
def calculator():
    print("Welcome to Simple Calculator!")

    while True:
        print("\nOperations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square Root")
        print("6. Exponentiation")
        print("7. Memory Clear")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice in ('1', '2', '3', '4', '6'):
            try:
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
                elif choice == '6':
                    print("Result:", power(num1, num2))
            except ValueError as ve:
                print("Error:", ve)
            except Exception as e:
                print("Error occurred:", e)

        elif choice == '5':
            try:
                num = float(input("Enter number to find square root: "))
                print("Result:", square_root(num))
            except ValueError as ve:
                print("Error:", ve)
            except Exception as e:
                print("Error occurred:", e)

        elif choice == '7':
            memory.clear()
            print("Memory cleared.")

        elif choice == '8':
            print("Thank you for using Simple Calculator. Goodbye!")
            break

        else:
            print("Invalid input. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    calculator()
