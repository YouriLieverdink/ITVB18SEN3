from itertools import permutations


def is_valid(permutation):
    # Loes woont niet op de bovenste verdieping.
    # Niels woont niet op de bovenste verdieping.
    if permutation[4] == 'L' or permutation[4] == 'N':
        return False

    # Marja woont niet op de begane grond.
    # Niels woont niet op de begane grond.
    if permutation[0] == 'M' or permutation[0] == 'N':
        return False

    # Erik woont tenminste één verdieping hoger dan Marja.
    e, m = permutation.index('E'), permutation.index('M')
    if (m + 1) > e:
        return False

    # Joep woont niet op een verdieping één hoger of lager dan Niels.
    j, n = permutation.index('J'), permutation.index('N')
    if (j + 1 == n) or (j - 1 == n):
        return False

    # Niels woont niet op een verdieping één hoger of lager dan Marja.
    if (n + 1 == m) or (n - 1 == m):
        return False

    return True


def solve():
    # Solve the floor puzzle.
    people = ('L', 'M', 'N', 'E', 'J')

    # Walk through every possible permutation.
    for permutation in list(permutations(people)):

        if is_valid(permutation):
            print('Valid:', permutation)


if __name__ == '__main__':
    solve()
