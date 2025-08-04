"""
Tic-Tac-Toe Game
================

A simple, interactive, and visually enhanced 3x3 Tic-Tac-Toe game for two players in the terminal.

Features:
---------
- Two-player mode with custom player names (entered once per session).
- Random selection of the starting player.
- Large, easy-to-read board display with coordinates.
- Input validation for moves (row and column must be 1-3 and cell must be empty).
- Fun and engaging messages for wins and draws, including emojis.
- Option to play multiple rounds without re-entering player names.
- Clean screen between turns for a better user experience.

How to Play:
------------
1. Run the script in a terminal.
2. Enter names for Player 'X' and Player 'O' when prompted.
3. The game randomly selects who goes first.
4. On your turn, enter your move as "row,col" (e.g., 2,3 for row 2, column 3).
5. The game checks for a winner or a draw after each move.
6. After the game ends, you can choose to play again or exit.

Functions:
----------
- clear_screen(): Clears the terminal screen for better readability.
- print_board(board): Displays the current state of the board in a large, clear format.
- check_winner(board, player): Checks if the given player has won.
- is_full(board): Checks if the board is full (draw).
- get_move(player_name, board): Prompts the player for a valid move.
- play_game(player_names): Runs a single game session.
- main(): Handles player name input and manages multiple game sessions.

Requirements:
-------------
- Python 3.x
- Works on Windows, macOS, and Linux terminals.

Author:
-------
- Adapted and enhanced by [Your Name], 2025

"""

import random
import os

def clear_screen():
    """
    Clears the terminal screen for better readability.
    Uses 'cls' for Windows and 'clear' for other OS.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    """
    Prints the current state of the Tic-Tac-Toe board in a large, clear format.
    Shows row and column numbers for easy reference.
    """
    print("\n      1     2     3")
    print("    ┌─────┬─────┬─────┐")
    for idx, row in enumerate(board):
        row_display = f" {idx+1}  │"
        for cell in row:
            row_display += f"  {cell}  │"
        print(row_display)
        if idx < 2:
            print("    ├─────┼─────┼─────┤")
    print("    └─────┴─────┴─────┘\n")

def check_winner(board, player):
    """
    Checks if the specified player ('X' or 'O') has won the game.
    Returns True if the player has three in a row, column, or diagonal.
    """
    for i in range(3):
        # Check rows and columns
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    """
    Checks if the board is full (i.e., no empty spaces left).
    Returns True if the board is full, indicating a draw.
    """
    return all(cell != " " for row in board for cell in row)

def possible_win(board, player):
    """
    Checks if the given player can still possibly win with the remaining moves.
    Returns True if there is at least one line (row, column, or diagonal)
    where the player can still get three in a row.
    """
    # Check rows
    for row in board:
        if not any(cell == (('O' if player == 'X' else 'X')) for cell in row):
            return True
    # Check columns
    for col in range(3):
        if not any(board[row][col] == (('O' if player == 'X' else 'X')) for row in range(3)):
            return True
    # Check diagonals
    if not any(board[i][i] == (('O' if player == 'X' else 'X')) for i in range(3)):
        return True
    if not any(board[i][2 - i] == (('O' if player == 'X' else 'X')) for i in range(3)):
        return True
    return False

def both_players_can_win(board):
    """
    Checks if at least one player can still possibly win.
    If neither player can win, returns False.
    """
    return possible_win(board, 'X') or possible_win(board, 'O')

def get_move(player_name, board):
    """
    Prompts the player for a move in the format 'row,col'.
    Validates the input and ensures the chosen cell is empty.
    Returns a tuple (row, col) for the move.
    """
    while True:
        try:
            move = input(f"{player_name}, enter your move as row,col (e.g., 2,3): ")
            row, col = [int(x.strip()) - 1 for x in move.split(",")]
            if row not in range(3) or col not in range(3):
                print("Coordinates must be between 1 and 3. Try again.")
                continue
            if board[row][col] != " ":
                print("Oops! That cell is already taken. Try another one.")
                continue
            return row, col
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as two numbers separated by a comma (e.g., 1,3).")

def play_game(player_names):
    """
    Runs a single session of the Tic-Tac-Toe game.
    Alternates turns between players, updates the board, and checks for a winner or draw.
    Displays the board and messages after each move.
    If neither player can possibly win with the remaining moves, declares a draw early.
    """
    clear_screen()
    print("🎮 Welcome to Tic-Tac-Toe! 🎮\n")
    players = ["X", "O"]
    turn = random.randint(0, 1)
    print(f"\n{player_names[turn]} ({players[turn]}) will start first!\n")
    input("Press Enter to start the game...")

    board = [[" " for _ in range(3)] for _ in range(3)]
    move_count = 0

    while True:
        clear_screen()
        print_board(board)
        player = players[turn % 2]
        player_name = player_names[turn % 2]
        print(f"Turn {move_count + 1}: {player_name} ({player})")
        row, col = get_move(player_name, board)
        board[row][col] = player
        move_count += 1

        if check_winner(board, player):
            clear_screen()
            print_board(board)
            print(f"🎉 Congratulations, {player_name}! You win! 🏆\n")
            break
        if is_full(board):
            clear_screen()
            print_board(board)
            print("🤝 It's a draw! Well played both!\n")
            break
        # Enhanced: If neither player can possibly win, declare draw early
        if not both_players_can_win(board):
            clear_screen()
            print_board(board)
            print("🤝 No possible way for either player to win! It's a draw!\n")
            break

        turn += 1

def main():
    """
    Main function to start the game.
    Prompts for player names once, then manages multiple game sessions.
    """
    clear_screen()
    print("🎮 Welcome to Tic-Tac-Toe! 🎮\n")
    player_names = []
    for symbol in ["X", "O"]:
        name = input(f"Enter name for Player '{symbol}': ").strip() or f"Player {symbol}"
        player_names.append(name)
    while True:
        play_game(player_names)
        again = input("Would you like to play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing! Goodbye! 👋")
            break

if __name__ == "__main__":
    main()