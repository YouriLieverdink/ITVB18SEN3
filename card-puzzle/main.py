import time
from itertools import permutations

from constants import NEIGHBOURS


def neighbours(i, b):
    # Returns a neighbouring cards.
    return [b[x] for x in NEIGHBOURS.get(i)]


def is_valid(b):
    # Check whether a provided board is valid.
    n = len(b)

    for i in range(n):
        # Retrieve the card.
        c, neighbouring = b[i], neighbours(i, b)

        # Two cards on the same type can't be neighbours.
        if c in neighbouring:
            return False

        # Every Ace is adjacent to a King.
        if (c == 'A') and ('K' not in neighbouring):
            return False

        # Every King is adjacent to a Queen.
        if (c == 'K') and ('Q' not in neighbouring):
            return False

        # Every Queen is adjacent to a Farmer.
        if (c == 'Q') and ('J' not in neighbouring):
            return False

        # Every Ace is not adjecent to a Queen.
        if (c == 'A') and ('Q' in neighbouring):
            return False

    return True


def brute_force(b):
    solutions = set()

    # Find the solution to the problem using brute force.
    for board in list(permutations(b)):
        if is_valid(board):
            solutions.add(board)

    return solutions


def solve(alg, b):
    # Find the solution using the provided algorithm.
    t0 = time.process_time()
    result = alg(b)
    t1 = time.process_time()

    print('Found {} solutions in {:.3f} seconds using {}.'.format(
        len(result), t1 - t0, alg.__name__)
    )


if __name__ == '__main__':
    # Start the script.
    b = ('A', 'A', 'K', 'K', 'Q', 'Q', 'J', 'J')
    solve(brute_force, b)
