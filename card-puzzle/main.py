import time
from itertools import permutations

from constants import CARDS, NEIGHBOURS


def neighbours(i, b):
    # Returns a neighbouring cards.
    return [b[x] for x in NEIGHBOURS.get(i)]


def is_valid(b):
    # Check whether a provided board is valid.
    n = len(b)

    for i in range(n):
        # Retrieve the card.
        c, peers = b[i], neighbours(i, b)

        # Two cards on the same type can't be neighbours.
        if (c != '.') and (c in peers):
            return False

        # Every Ace is adjacent to a King.
        if (c == 'A') and ('K' not in peers and '.' not in peers):
            return False

        # Every King is adjacent to a Queen.
        if (c == 'K') and ('Q' not in peers and '.' not in peers):
            return False

        # Every Queen is adjacent to a Farmer.
        if (c == 'Q') and ('J' not in peers and '.' not in peers):
            return False

        # Every Ace is not adjecent to a Queen.
        if (c == 'A') and ('Q' in peers):
            return False

    return True


def brute_force(b, s, domain=CARDS):
    # Find solutions using brute force.
    for board in list(permutations(domain)):
        if is_valid(board):
            s.add(board)


def dfs(b, s, i=0, domain=CARDS):
    # Find solutions using dfs and back-tracking.
    if is_valid(b):
        # Check if all keys have a value.
        if b.count('.') == 0:
            # Found a solution!
            return True

        # Try all values from the domain.
        for c in domain:
            # Assign the variable.
            b[i] = c
            domain.remove(c)

            # Start the recursive call.
            if dfs(b, s, i + 1, domain):
                # Found a solution!
                s.add(str(b))

            # Undo the assignment.
            b[i] = '.'
            domain.append(c)


def solve(alg, b):
    # Find the solution using the provided algorithm.
    t0 = time.process_time()

    solutions = set()
    alg(b, solutions)

    t1 = time.process_time()

    for s in solutions:
        print(s)

    print('Found {} solutions in {:.3f} seconds using {}.\n'.format(
        len(solutions), t1 - t0, alg.__name__)
    )


if __name__ == '__main__':
    # Start the script.
    b = ['.', '.', '.', '.', '.', '.', '.', '.']

    solve(brute_force, b)
    solve(dfs, b)
