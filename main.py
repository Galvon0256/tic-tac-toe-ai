def get_valid_moves(board):
    """Returns a list of valid moves on the board."""
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def print_board(board):
    """Prints the current state of the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def is_winner(board, player):
    """Checks if the given player has won the game."""
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # Rows
            return True
        if all(board[j][i] == player for j in range(3)):  # Columns
            return True
    # Diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    """Checks if the game is a draw."""
    return all(cell != " " for row in board for cell in row)


def minimax(board, depth, is_maximizing):
    """
    Minimax algorithm for Tic Tac Toe.
    - board: Current state of the game board.
    - depth: Current depth of the recursion.
    - is_maximizing: True if AI is maximizing, False if minimizing.
    """
    # Check for terminal states (win/loss/draw)
    if is_winner(board, "O"):  # AI wins
        return 10 - depth
    if is_winner(board, "X"):  # Player wins
        return depth - 10
    if is_draw(board):  # Draw
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for row, col in get_valid_moves(board):
            board[row][col] = "O"  # AI makes a move
            score = minimax(board, depth + 1, False)  # Recur for opponent
            board[row][col] = " "  # Undo the move
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for row, col in get_valid_moves(board):
            board[row][col] = "X"  # Opponent makes a move
            score = minimax(board, depth + 1, True)  # Recur for AI
            board[row][col] = " "  # Undo the move
            best_score = min(best_score, score)
        return best_score


def find_best_move(board):
    """
    Finds the best move for the AI player using the minimax algorithm.
    - board: Current state of the game board.
    """
    best_score = float('-inf')
    best_move = None

    for row, col in get_valid_moves(board):
        board[row][col] = "O"  # AI makes a move
        score = minimax(board, 0, False)  # Calculate score for this move
        board[row][col] = " "  # Undo the move
        if score > best_score:
            best_score = score
            best_move = (row, col)

    return best_move

def play_game_with_ai():
    """Tic Tac Toe game where the AI plays as O."""
    board = [[" " for _ in range(3)] for _ in range(3)]  # 3x3 empty board
    current_player = "X"

    print("Welcome to Tic Tac Toe with AI!")
    print_board(board)

    while True:
        if current_player == "X":
            # Human player's turn
            print("\nYour turn (X).")
            move = None
            while move not in get_valid_moves(board):
                try:
                    row, col = map(int, input("Enter your move (row and column: 0 1): ").split())
                    move = (row, col)
                except ValueError:
                    print("Invalid input. Enter row and column numbers separated by a space.")
            board[move[0]][move[1]] = "X"
        else:
            # AI's turn
            print("\nAI's turn (O).")
            move = find_best_move(board)
            board[move[0]][move[1]] = "O"

        print_board(board)

        # Check for win or draw
        if is_winner(board, current_player):
            print(f"\n{current_player} wins!")
            break
        if is_draw(board):
            print("\nIt's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game_with_ai()
