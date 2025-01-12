# 2. Simple ATM Simulation
# Objective: Create a simulation for basic ATM operations.
# Steps:
# 1. Initialize a default balance (e.g., 10,000).
# 2. Provide a menu with options:
# o Check balance.
# o Deposit money.
# o Withdraw money.
# o Exit.
# 3. For deposit, add the entered amount to the balance.
# 4. For withdrawal, ensure the entered amount is less 



def atm_simulation():
    balance = 10000  # Initialize default balance

    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print(f"Your current balance is: {balance}")

        elif choice == "2":
            deposit = input("Enter amount to deposit: ")
            if deposit.isdigit():
                deposit = float(deposit)
                if deposit > 0:
                    balance += deposit
                    print(f"{deposit} has been deposited. New balance: {balance}")
                else:
                    print("Deposit amount must be positive.")
            else:
                print("Invalid input! Please enter a valid number.")

        elif choice == "3":
            withdraw = input("Enter amount to withdraw: ")
            if withdraw.isdigit():
                withdraw = float(withdraw)
                if 0 < withdraw <= balance:
                    balance -= withdraw
                    print(f"{withdraw} has been withdrawn. New balance: {balance}")
                elif withdraw > balance:
                    print("Insufficient balance.")
                else:
                    print("Withdrawal amount must be positive.")
            else:
                print("Invalid input! Please enter a valid number.")

        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice! Please select an option between 1 and 4.")

# Run the ATM simulation
atm_simulation()
