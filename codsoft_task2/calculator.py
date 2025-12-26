# Task 2: Simple Calculator
# Python Programming Internship

def calculator():
    print("----- SIMPLE CALCULATOR -----")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter your choice (1/2/3/4): ")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"Result: {num1} + {num2} = {num1 + num2}")

        elif choice == '2':
            print(f"Result: {num1} - {num2} = {num1 - num2}")

        elif choice == '3':
            print(f"Result: {num1} * {num2} = {num1 * num2}")

        elif choice == '4':
            if num2 != 0:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")

        else:
            print("Invalid choice! Please choose between 1 and 4.")

    except ValueError:
        print("Invalid input! Please enter numeric values only.")


# Program execution
calculator()
