import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
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
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def get_move(player_name, board):
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

        turn += 1

def main():
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