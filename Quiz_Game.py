'''Quiz Game
Objective: Create a multiple-choice quiz on any topic.
Features: Track the score, display correct answers, and provide a final score summary.'''

import random

# Define the quiz questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is the largest ocean in the world?",
        "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
        "answer": "Pacific Ocean"
    },
    {
        "question": "What is the national animal of the United States?",
        "options": ["Bald Eagle", "Giraffe", "Elephant", "Gorilla"],
        "answer": "Bald Eagle"
    },
    {
        "question": "What is the national dish of the United States?",
        "options": ["Burger", "Pizza", "Fries", "Tacos"],
        "answer": "Burger"
    }
]

def quiz_game():
    # Shuffle the questions for randomness
    random.shuffle(questions)

    # Initialize the score
    score = 0
    num_questions = len(questions)

    # Loop through each question
    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for idx, option in enumerate(q['options'], 1):
            print(f"{idx}. {option}")

        # Validate user input
        while True:
            try:
                user_answer = int(input("Enter your answer (1-4): "))
                if 1 <= user_answer <= 4:
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a valid number between 1 and 4.")

        # Check the answer
        if q['options'][user_answer - 1] == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {q['answer']}")
        print()  # Blank line for better readability

    # Display the final score
    print(f"Quiz Over! You scored {score}/{num_questions} points.")

# Run the quiz game
if __name__ == "__main__":
    quiz_game()

