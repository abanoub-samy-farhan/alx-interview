#!/usr/bin/python3
"""
This Module is the module for the N queens problem
"""
import sys


def print_usage_and_exit(message):
    """Print error message and exit with status 1"""
    print(message)
    sys.exit(1)


def is_safe(board, row, col, n):
    """Check if placing a queen at (row, col) is safe"""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens_util(board, col, n, solutions):
    """Utility function to solve N-Queens recursively"""
    if col == n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, n, solutions)
            board[i][col] = 0


def solve_nqueens(n):
    """Solve the N-Queens problem and print solutions"""
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)
    for solution in solutions:
        print(solution)


def main():
    """Main function to parse arguments and run the solver"""
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N")

    try:
        n = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")

    if n < 4:
        print_usage_and_exit("N must be at least 4")

    solve_nqueens(n)


if __name__ == "__main__":
    main()
