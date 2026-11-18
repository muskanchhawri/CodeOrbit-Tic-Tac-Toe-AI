
# Tic-Tac-Toe with Simple AI
# CodeOrbit Tech Internship - Task 2

import random

# Create the game board
board = [" " for _ in range(9)]


# Display the board
def display_board():
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


# Check winning combinations
winning_combinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


# Check whether a player has won
def check_winner(symbol):
    for combination in winning_combinations:
        a, b, c = combination

        if board[a] == board[b] == board[c] == symbol:
            return True

    return False


# Simple AI for computer
def computer_move():

    # Rule 1: Check if computer can win
    for position in range(9):
        if board[position] == " ":
            board[position] = "O"

            if check_winner("O"):
                return

            board[position] = " "

    # Rule 2: Block player's winning move
    for position in range(9):
        if board[position] == " ":
            board[position] = "X"

            if check_winner("X"):
                board[position] = "O"
                return

            board[position] = " "

    # Rule 3: Choose center if available
    if board[4] == " ":
        board[4] = "O"
        return

    # Rule 4: Choose an empty corner
    corners = [0, 2, 6, 8]
    empty_corners = [
        position for position in corners
        if board[position] == " "
    ]

    if empty_corners:
        position = random.choice(empty_corners)
        board[position] = "O"
        return

    # Rule 5: Choose any remaining empty position
    empty_positions = [
        position for position in range(9)
        if board[position] == " "
    ]

    if empty_positions:
        position = random.choice(empty_positions)
        board[position] = "O"


# Main game
def play_game():

    print("Welcome to Tic-Tac-Toe!")
    print("You are X and Computer is O.")
    print("Choose a position from 1 to 9.")

    while True:

        display_board()

        # Player's turn
        try:
            position = int(input("Enter position (1-9): ")) - 1

        except ValueError:
            print("Please enter a valid number!")
            continue

        if position < 0 or position > 8:
            print("Choose a position between 1 and 9!")
            continue

        if board[position] != " ":
            print("This position is already occupied!")
            continue

        board[position] = "X"

        # Check player win
        if check_winner("X"):
            display_board()
            print("Congratulations! You Win!")
            break

        # Check draw
        if " " not in board:
            display_board()
            print("Game Draw!")
            break

        # Computer's turn
        print("Computer is making a move...")
        computer_move()

        # Check computer win
        if check_winner("O"):
            display_board()
            print("Computer Wins! Better Luck Next Time.")
            break

        # Check draw
        if " " not in board:
            display_board()
            print("Game Draw!")
            break

    print("Game Over!")


# Start the game
play_game()
