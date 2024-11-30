# Importing random module to generate random numbers
import random

# Function to generate random number
def generate_number():
    return random.randint(1, 100)

# Function to check if the guess is correct
def check_guess(guess, number, attempts):
    if guess == number:
        print("Congratulations! You guessed the number in", attempts, "attempts.")
        return True
    elif guess < number:
        print("Too low. Guess again.")
        return False
    else:
        print("Too high. Guess again.")
        return False

# Main function
def play_game():
    # Generate random number
    number = generate_number()
    # Initialize attempts counter
    attempts = 0
    # Loop until correct guess is made
    while True:
        # Get user input
        try:
            guess = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        # Increment attempts counter
        attempts += 1
        # Check if guess is correct
        if check_guess(guess, number, attempts):
            break
    # Ask if user wants to play again
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == "y":
        play_game()

# Call main function to start the game
play_game()
