def is_safe(board, row, col):
  """
  Checks if placing a queen at (row, col) is safe (no conflicts)

  Args:
      board: A 2D list representing the chessboard
      row: The row to place the queen
      col: The column to place the queen

  Returns:
      True if placing the queen is safe, False otherwise.
  """
  # Check row conflicts
  for i in range(col):
    if board[row][i] == 1:
      return False

  # Check diagonal conflicts (upward)
  i, j = row, col
  while i >= 0 and j >= 0:
    if board[i][j] == 1:
      return False
    i -= 1
    j -= 1

  # Check diagonal conflicts (downward)
  i, j = row, col
  while i < len(board) and j >= 0:
    if board[i][j] == 1:
      return False
    i += 1
    j -= 1

  return True

def solve_n_queens_backtracking(board, col):
  """
  Solves the N-Queens problem using Backtracking

  Args:
      board: A 2D list representing the chessboard
      col: The current column to place the queen

  Returns:
      True if a solution is found, False otherwise.
  """
  if col >= len(board):
    return True  # All queens placed successfully

  for row in range(len(board)):
    if is_safe(board, row, col):
      board[row][col] = 1  # Place the queen

      if solve_n_queens_backtracking(board, col + 1):
        return True  # Found a solution in this branch

      board[row][col] = 0  # Backtrack (remove the queen)

  return False  # No solution found in this branch

def print_solution(board):
  """
  Prints the chessboard with queens placed
  """
  for row in board:
    print(row)

def solve_n_queens(n):
  """
  Solves the N-Queens problem using Backtracking

  Args:
      n: The number of queens (board size)
  """
  board = [[0 for _ in range(n)] for _ in range(n)]
  if solve_n_queens_backtracking(board, 0):
    print_solution(board)
  else:
    print("No solution exists")

if __name__ == "__main__":
  n = int(input("Enter the number of queens: "))
  solve_n_queens(n)
