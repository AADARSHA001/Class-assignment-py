# 8. Currency Converter
# Objective: Create a program to convert amounts between currencies.
# Steps:
# 1. Use a dictionary to store exchange rates (e.g., USD to INR, USD to EUR).
# 2. Allow the user to select the currency pair (e.g., USD to INR).
# 3. Take an amount as input.
# 4. Multiply the amount by the exchange rate and display the result.
# 5. Allow the user to convert multiple times in a loop.

def currency_converter():
    # Exchange rates stored in a dictionary
    exchange_rates = {
        "USD_to_INR": 83.0,
        "USD_to_EUR": 0.92,
        "INR_to_USD": 0.012,
        "EUR_to_USD": 1.09,
        "INR_to_EUR": 0.011,
        "EUR_to_INR": 90.0
    }
    
    while True:
        print("\nAvailable currency pairs:")
        for pair in exchange_rates.keys():
            print(pair)
        
        # User selects the currency pair
        currency_pair = input("\nEnter the currency pair (e.g., USD_to_INR): ").strip()
        
        # Check if the selected pair is valid
        if currency_pair in exchange_rates:
            try:
                # Input the amount to be converted
                amount = float(input(f"Enter the amount in {currency_pair.split('_to_')[0]}: "))
                # Calculate the converted amount
                converted_amount = amount * exchange_rates[currency_pair]
                # Display the result
                print(f"{amount} in {currency_pair.split('_to_')[0]} is {converted_amount:.2f} in {currency_pair.split('_to_')[1]}.")
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        else:
            print("Invalid currency pair. Please try again.")
        
        # Ask if the user wants to continue
        continue_choice = input("\nDo you want to convert another amount? (yes/no): ").strip().lower()
        if continue_choice != "yes":
            print("Thank you for using the currency converter!")
            break

# Run the currency converter
currency_converter()

