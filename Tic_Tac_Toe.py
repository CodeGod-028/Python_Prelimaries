# Simple Tic Tac Toe Game for Two Players

def display_board(board):
    """Display the current state of the board."""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def is_winner(board, player):
    """Check if the player has won."""
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[pos] == player for pos in combo) for combo in win_combinations)

def is_full(board):
    """Check if the board is full."""
    return ' ' not in board

def get_move(player, board):
    """Get a valid move from the player."""
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid move. Please enter a number between 1 and 9.")
            elif board[move] != ' ':
                print("This position is already taken. Choose another.")
            else:
                return move
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def play_game():
    """Main function to play the game."""
    print("Welcome to Tic Tac Toe!")
    print("Player 1 is X and Player 2 is O")
    print("Take turns placing your marks. The first to get three in a row wins!")

    # Initialize the board
    board = [' '] * 9
    current_player = 'X'

    # Display the initial board
    display_board(board)

    while True:
        # Get the player's move
        move = get_move(current_player, board)
        board[move] = current_player

        # Display the updated board
        display_board(board)

        # Check if the player has won
        if is_winner(board, current_player):
            print(f"Congratulations! Player {current_player} wins!")
            break

        # Check for a tie
        if is_full(board):
            print("It's a tie!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
