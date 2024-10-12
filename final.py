def print_board(board):
    """Print the current state of the board."""
    print("Current board:")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("--------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("--------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_winner(board):
    """Check rows, columns, and diagonals for a winner."""
    winning_combos = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    for combo in winning_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return True
    return False

def is_board_full(board):
    """Check if the board is full."""
    return all(cell != " " for cell in board)

def play_game():
    """Play the Tic Tac Toe game."""
    board = [" " for _ in range(9)]
    players = ["X", "O"]
    current_player_index = 0

    while True:
        print_board(board)
        print(f"Player {players[current_player_index]}, enter your move (1-9), or 'q' to quit: ")

        try:
            move = input("Enter the cell number or 'q': ")
            if move.lower() == 'q':
                print("Game quit.")
                break

            move = int(move)
            if move < 1 or move > 9:
                print("Invalid move. Please enter a number between 1 and 9.")
                continue

            if board[move - 1] != " ":
                print("Cell already taken. Try again.")
                continue

            board[move - 1] = players[current_player_index]

            if check_winner(board):
                print_board(board)
                print(f"Player {players[current_player_index]} wins!")
                break

            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            current_player_index = (current_player_index + 1) % 2

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9 or 'q' to quit.")

if __name__ == "__main__":
    play_game()
