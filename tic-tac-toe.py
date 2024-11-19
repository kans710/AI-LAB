import math

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

def is_moves_left(board):
    for row in board:
        if '_' in row:
            return True
    return False

def evaluate(board):
    # Check rows for a win
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '_':
            return 10 if row[0] == 'O' else -10

    # Check columns for a win
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '_':
            return 10 if board[0][col] == 'O' else -10

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '_':
        return 10 if board[0][0] == 'O' else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '_':
        return 10 if board[0][2] == 'O' else -10

    return 0

def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    # If someone has won
    if score == 10:
        return score - depth
    if score == -10:
        return score + depth

    # If no moves left
    if not is_moves_left(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = '_'
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = '_'
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'O'
                move_val = minimax(board, 0, False)
                board[i][j] = '_'
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    return best_move

def main():
    board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Player move
        print("\nYour move (Enter row and column: 0 1 for row 0, column 1):")
        row, col = map(int, input().split())
        if board[row][col] != '_':
            print("Invalid move. Try again.")
            continue
        board[row][col] = 'X'

        # Check if player wins
        if evaluate(board) == -10:
            print_board(board)
            print("You win!")
            break

        # Check for a draw
        if not is_moves_left(board):
            print_board(board)
            print("It's a draw!")
            break

        # Computer move
        print("\nComputer's move:")
        move = find_best_move(board)
        board[move[0]][move[1]] = 'O'

        # Print the board after computer's move
        print_board(board)

        # Check if computer wins
        if evaluate(board) == 10:
            print("Computer wins!")
            break

        # Check for a draw
        if not is_moves_left(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
