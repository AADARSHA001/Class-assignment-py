# 9. Unit Converter
# Objective: Create a program to convert between units.
# Steps:
# 1. Display a menu with options (e.g., km to miles, Celsius to Fahrenheit).
# 2. Take the input value.
# 3. Perform the conversion using the relevant formula:
# o Miles=Kilometers×0.621371\text{Miles} = \text{Kilometers} \times 0.621371
# o Fahrenheit=(Celsius×9/5)+32\text{Fahrenheit} = (\text{Celsius} \times 9/5) + 32
# 4. Display the result.
# 5. Allow the user to perform multiple conversions in a loop.


def unit_converter():
    def display_menu():
        print("\nUnit Converter Menu:")
        print("1. Kilometers to Miles")
        print("2. Celsius to Fahrenheit")
        print("3. Exit")

    def km_to_miles(km):
        return km * 0.621371

    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    print("Welcome to the Unit Converter!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "3":
            print("\nThank you for using the Unit Converter. Goodbye!")
            break

        if choice == "1":
            try:
                km = float(input("Enter the distance in kilometers: "))
                miles = km_to_miles(km)
                print(f"{km} kilometers is equal to {miles:.2f} miles.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == "2":
            try:
                celsius = float(input("Enter the temperature in Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"{celsius}°C is equal to {fahrenheit:.2f}°F.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        else:
            print("Invalid choice. Please select a valid option.")

# Run the Unit Converter
unit_converter()
