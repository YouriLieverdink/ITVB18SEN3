
def empty(b):
    """Return a heuristic value based on the number of empty spaces."""
    value = 0

    for row in b:
        value += row.count(0)

    return value


def weights(b):
    """Return a heuristic value based on the weights of specified locations."""
    value, n = 0, len(b)

    weights = [
        [2048, 1024, 64, 32],
        [512, 128, 16, 2],
        [256, 8, 2, 1],
        [4, 2, 1, 1]
    ]

    for i in range(n):
        for j in range(n):
            value += (b[i][j] * weights[i][j])

    return value


def monotonicity(b):
    """Return a heuristic value based on the increase/decrease in numbers in rows/columns."""
    value, n = 0, len(b)

    for row in b:
        # Calculate the difference.
        diff = row[0] - row[1]

        for i in range(n - 1):
            # Check whether the difference of the following cells is less than 0.
            if (row[i] - row[i + 1]) * diff <= 0:
                value += 1

            # Update the diff variable.
            diff = row[i] - row[i + 1]

    for j in range(n):
        # Calculate the difference.
        diff = b[0][j] - b[1][j]

        for k in range(n - 1):
            # Check whether the difference of the following cells is less than 0.
            if (b[i][j] - b[k + 1][j]) * diff <= 0:
                value += 1

            # Update the diff variable.
            diff = b[k][j] - b[k + 1][j]

    return value


def position(b):
    """Return a heuristic value based on the position of the largest value on the board."""
    value, tile, n = 0, -1, len(b)

    # Retrieve the largest value.
    for row in b:
        for cell in row:
            if cell > tile:
                tile = cell

    # Check if the tile is in the desired location.
    if b[0][0] == tile:
        value += (1024 * tile)

    return value


def heuristic(b):
    # Computes the heuristic of the board based on a set strategy.
    values = {
        'empty': {
            'value': empty(b),
            'weight': 3,
        },
        'weights': {
            'value': weights(b),
            'weight': 7,
        },
        'monotonicity': {
            'value': monotonicity(b),
            'weight': 2,
        },
        'position': {
            'value': position(b),
            'weight': 9,
        },
    }

    value = 0

    for key in values.keys():
        value += (values[key]['value'] * values[key]['weight'])

    return value
