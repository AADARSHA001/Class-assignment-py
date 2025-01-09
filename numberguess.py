# 3. Number Guessing Game
# Objective: Build a guessing game where the user guesses a randomly generated number.
# Steps:
# 1. Use Python’s random module to generate a number between 1 and 100.
# 2. Allow the user to guess the number.
# 3. Provide feedback ("Too high" or "Too low").
# 4. Limit the number of attempts to 5.
# 5. Display a success or failure message at the end.

import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)  # Generate a random number between 1 and 100
    attempts = 5  # Maximum number of attempts

    print("\nWelcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it.")

    while attempts > 0:
        guess = input("Enter your guess: ")

        if guess.isdigit():
            guess = int(guess)

            if guess == number_to_guess:
                print("Congratulations! You guessed the correct number.")
                break
            elif guess < number_to_guess:
                print("Too low!")
            else:
                print("Too high!")

            attempts -= 1
            if attempts > 0:
                print(f"You have {attempts} attempts left.")
            else:
                print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")
        else:
            print("Invalid input! Please enter a number between 1 and 100.")

# Run the Number Guessing Game
number_guessing_game()
