import math

import constants as c


def parse_board(b_str):
    # Parse the provided board string and return a 2-dimensional array.
    b, t, n = [], [], len(b_str)

    for i in range(n):

        if i % 9 == 0 and i != 0:
            b.append(t)
            t = []

        t.append(b_str[i])

    b.append(t)

    return b


def print_board(b):
    # Prints the provided board.
    n = len(b)

    print()

    for i in range(n):

        if i in [3, 6]:
            print('----- + ----- + -----')

        for j in range(n):

            if j in [3, 6]:
                print('|', end=' ')

            print(b[i][j], end=' ')
        print()

    print()


def peers(p, b):
    # Returns the positions of the peers for the provided position.
    return []


def dfs(b):
    # Solves the sudoku using deep first search.
    return b


if __name__ == '__main__':
    # Start the script.
    b = parse_board(c.B1)
    solution = dfs(b)

    print_board(solution)
