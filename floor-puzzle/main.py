from itertools import permutations


def is_valid(combination):
    # Loes woont niet op de bovenste verdieping.
    # Niels woont niet op de bovenste verdieping.
    if combination[4] == 'L' or combination[4] == 'N':
        return False

    # Marja woont niet op de begane grond.
    # Niels woont niet op de begane grond.
    if combination[0] == 'M' or combination[0] == 'N':
        return False

    # Erik woont tenminste één verdieping hoger dan Marja.
    e, m = combination.index('E'), combination.index('M')
    if (m + 1) > e:
        return False

    # Joep woont niet op een verdieping één hoger of lager dan Niels.
    j, n = combination.index('J'), combination.index('N')
    if (j + 1 == n) or (j - 1 == n):
        return False

    # Niels woont niet op een verdieping één hoger of lager dan Marja.
    if (n + 1 == m) or (n - 1 == m):
        return False

    return True


def solve():
    # Solve the floor puzzle.
    people = ('L', 'M', 'N', 'E', 'J')

    # Walk through every possible combination.
    for combination in list(permutations(people)):

        if is_valid(combination):
            print('Valid:', combination)


if __name__ == '__main__':
    solve()
