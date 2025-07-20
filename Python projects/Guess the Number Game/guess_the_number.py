# guess_the_number.py

import random

def guess_the_number_game():
    """
    Implements the "Guess the Number" game.
    The computer chooses a random number, and the user tries to guess it.
    """
    print("----- Guess the Number Game -----")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it?")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess_str = input("Enter your guess: ")
            guess = int(guess_str)
            attempts += 1

            if guess < 1 or guess > 100:
                print("Your guess is out of range. Please guess a number between 1 and 100.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number ({secret_number}) in {attempts} attempts!")
                break # Exit the loop if the guess is correct

        except ValueError:
            print("Invalid input. Please enter a whole number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

    print("\nThanks for playing!")

if __name__ == "__main__":
    guess_the_number_game()
