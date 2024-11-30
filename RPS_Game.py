'''.Rock, Paper, Scissors Game
Objective: Simulate the classic game against the computer.
Features: Use random choice for the computer and display results ("Win", "Lose", or "Tie").'''

# Importing random module to generate random choices
import random

# Function to display the result of the game
def display_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("You lose!")

# Function to get user input
def get_user_input():    
    user_choice = input("Enter your choice (rock, paper, or scissors): ")
    return user_choice

# Function to get computer input
def get_computer_input():
    computer_choice = random.choice(["rock", "paper", "scissors"])
    return computer_choice

# Main function to run the game
def play_game():
    user_choice = get_user_input()
    computer_choice = get_computer_input()
    display_result(user_choice, computer_choice)

# Calling the main function to start the game
play_game()