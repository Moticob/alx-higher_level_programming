#!/usr/bin/env python3
"""
N queens problem solver.

Usage: nqueens N

Where N is an integer greater or equal to 4.

The program should print all possible solutions to the problem.

One solution per line.

Format: `[[row1, col1], [row2, col2], ...]`

You don't have to print the solutions in a specific order.

You are only allowed to import the `sys` module.

Read: Queen, Backtracking.
"""


import sys


def is_safe(board, row, col, n):
  """
  Checks if it is safe to place a queen at (row, col)

  Args:
    board: The NxN chessboard
    row: The row where the queen is being placed
    col: The column where the queen is being placed

  Returns:
    True if it is safe to place the queen, False otherwise
  """

  # Check if there is a queen in the same column
  for i in range(row):
    if board[i][col] == 1:
      return False

  # Check upper left diagonal
  for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
    if board[i][j] == 1:
      return False

  # Check upper right diagonal
  for i, j in zip(range(row, -1, -1), range(col, n)):
    if board[i][j] == 1:
      return False

  return True


def solve_nqueens(board, n, row):
  """
  Solves the N queens problem recursively

  Args:
    board: The NxN chessboard
    n: The size of the chessboard
    row: The current row

  Returns:
    A list of all solutions found
  """

  if row == n:
    return [[row, col] for col in range(n)]

  solutions = []
  for col in range(n):
    if is_safe(board, row, col, n):
      board[row][col] = 1
      solutions.extend(solve_nqueens(board, n, row + 1))
      board[row][col] = 0

  return solutions


def main():
  """
  The main function
  """

  if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} N")
    sys.exit(1)

  n = int(sys.argv[1])
  if not isinstance(n, int) or n < 4:
    print(f"N must be an integer greater or equal to 4")
    sys.exit(1)

  board = [[0] * n for _ in range(n)]
  solutions = solve_nqueens(board, n, 0)

  for solution in solutions:
    print(solution)


if __name__ == "__main__":
  main()
