#!/usr/bin/env python3
"""
N Queens Puzzle
"""

import sys


def solve(row, column):
    """
    Function solve definintion
    initializes the solver and iteratively places queens
    On the chessboard by calling the place_queen function
    """
    solver = [[]]
    for q in range(row):
        solver = place_queen(q, column, solver)
    return solver


def place_queen(q, column, prev_solver):
    """
    Funtion place_queen definition
    checks for safety using the is_safe function
    And generates new solutions.
    """
    solver_queen = []
    for array in prev_solver:
        for x in range(column):
            if is_safe(q, x, array):
                solver_queen.append(array + [x])
    return solver_queen


def is_safe(q, x, array):
    """
    This function checks if placing a queen at position (q, x)
    On the chessboard is safe by verifying that no two queens
    Threaten each other.
    """
    if x in array:
        return (False)
    else:
        return all(abs(array[column] - x) != q - column
                   for column in range(q))


def init():
    """
    Checks for valid input and exits the program if the input
    Is not appropriate.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        the_queen = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if the_queen < 4:
        print("N must be at least 4")
        sys.exit(1)
    return(the_queen)


def n_queens():
    """
    Main function that initiates the solution process
    """
    the_queen = init()
    solver = solve(the_queen, the_queen)
    for array in solver:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)


if __name__ == "__main__":
    """
    Ensures that the n_queens() function is called only
    If the script is run directly (not imported as a module)
    """
    n_queens()
