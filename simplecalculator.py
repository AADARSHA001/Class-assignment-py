# 5. Simple Calculator
# Objective: Design a program for basic arithmetic operations.
# Steps:
# 1. Display a menu with options: addition, subtraction, multiplication, and division.
# 2. Take two numbers as input.
# 3. Perform the selected operation and display the result.
# 4. Handle division by zero gracefully.
# 5. Allow the user to perform multiple operations in a loop.

def calculator():
    print("Welcome to the Simple Calculator!")
    
    while True:
        # Display menu
        print("\nMenu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        # Take user's choice
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "5":
            print("Thank you for using the calculator. Goodbye!")
            break
        
        if choice not in {"1", "2", "3", "4"}:
            print("Invalid choice. Please select a valid option.")
            continue
        
        # Take two numbers as input
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        
        # Perform the selected operation
        if choice == "1":
            result = num1 + num2
            print(f"The result of addition: {num1} + {num2} = {result}")
        elif choice == "2":
            result = num1 - num2
            print(f"The result of subtraction: {num1} - {num2} = {result}")
        elif choice == "3":
            result = num1 * num2
            print(f"The result of multiplication: {num1} * {num2} = {result}")
        elif choice == "4":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"The result of division: {num1} / {num2} = {result}")
        
        # Ask if the user wants to continue
        continue_choice = input("\nDo you want to perform another operation? (yes/no): ").strip().lower()
        if continue_choice != "yes":
            print("Thank you for using the calculator. Goodbye!")
            break

# Run the calculator
calculator()
