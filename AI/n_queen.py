# User input for the number of queens
N = int(input("Enter number of queens: "))

# Create an N x N board initialized with 0 (no queen placed)
board = [[0] * N for _ in range(N)]

# Function to print the board
def print_board(board):
    for row in board:
        print(row)

# Function to check if placing a queen at (row, col) is safe
def is_safe(row, col):
    # Check the same column and same row
    for i in range(N):
        if board[i][col] == 1 or board[row][i] == 1:
            return False

    # Check diagonals
    for i in range(N):
        for j in range(N):
            # If in same diagonal (i + j == row + col OR i - j == row - col)
            if row + col == i + j or row - col == i - j:
                if board[i][j] == 1:
                    return False

    return True

# Recursive backtracking function to place queens
def solve_n_queens(remaining_queens):
    if remaining_queens == 0:
        return True  # All queens placed successfully

    for row in range(N):
        for col in range(N):
            if board[row][col] != 1 and is_safe(row, col):
                board[row][col] = 1  # Place queen
                if solve_n_queens(remaining_queens - 1):
                    return True
                board[row][col] = 0  # Backtrack

    return False

# Start the solving process
if solve_n_queens(N):
    print_board(board)
else:
    print("No solution exists")





# def is_safe(board, row, col, n):
#     # Check for this column on the upper side
#     for i in range(row):
#         if board[i] == col or \
#            board[i] - i == col - row or \
#            board[i] + i == col + row:
#             return False
#     return True

# def solve_nqueens(board, row, n):
#     if row == n:
#         print_board(board, n)
#         return True
    
#     for col in range(n):
#         if is_safe(board, row, col, n):
#             board[row] = col
#             if solve_nqueens(board, row + 1, n):
#                 return True
#             board[row] = -1  # backtrack
    
#     return False

# def print_board(board, n):
#     for i in range(n):
#         row = ['Q' if j == board[i] else '.' for j in range(n)]
#         print(' '.join(row))
#     print("\n")

# def nqueens(n):
#     board = [-1] * n
#     if not solve_nqueens(board, 0, n):
#         print("No solution exists")

# # Take input from the user
# n = int(input("Enter the value of n for N-Queens: "))
# nqueens(n)
