import numpy as np

# place triominoes in matrix 3 rows x 4 cols

NR_OF_COLS = 16  # 4 triominoes HB VB L RL + 12 cells
NR_OF_ROWS = 22  # 6*HB 4*VB 6*L 6*RL

triominoes = [np.array(piece) for piece in [
    # horizontal bar (HB)
    [[1, 1, 1]],
    # vertical bar (VB)
    [[1], [1], [1]],
    # normal L (L)
    [[1, 0], [1, 1]],
    # rotated L (RL)
    [[1, 1], [0, 1]]
]
]


def make_matrix(triominoes):

    # create and return matrix as input for alg-x
    # matrix has 22 rows x 16 cols
    # and has the following cols: HB VB L RL (0,0) (0,1) (0,2) (0,3) (1,0) .... (3,3)

    def all_positions(triominoes):
        # find all positions to place triomino T in matrix M (3 rows x 4 cols)
        rows, cols = triominoes.shape
        for i in range(3+1 - rows):
            for j in range(4+1 - cols):
                M = np.zeros((3, 4), dtype='int')
                # place T in M
                M[i:i+rows, j:j+cols] = triominoes
                yield M

    rows = []
    for i, P in enumerate(triominoes):
        # i points to the 4 triominoes HB VB L RL
        for A in all_positions(P):
            # add 4 zeros to each row
            A = np.append(np.zeros(4, dtype='int'), A)
            A[i] = 1
            rows.append(list(A))
    return rows


def prepare(mx):
    # note that when applying alg-x we're only interested in 1's
    # so we add 2 lists that define where the 1's are
    rows = mx
    # note that zip(*b) is the transpose of b
    cols = [list(i) for i in zip(*rows)]

    # print(np.array(rows))
    # print()

    def find_ones(rows):
        # returns indexes in rows where the ondes are
        # example: [[0, 3], [1, 3], [1, 2], [2]]
        lv_row_has_1_at = []
        for row in rows:
            x = []
            for i in range(len(row)):
                if row[i] == 1:
                    x.append(i)
            lv_row_has_1_at.append(x.copy())
        return lv_row_has_1_at

    # read-only list; example: [[0, 3], [1, 3], [1, 2], [2]]
    row_has_1_at = find_ones(rows)
    # read-only list; example: [[0], [1, 2], [2, 3], [0, 1]]
    col_has_1_at = find_ones(cols)

    # if there's a col without ones, then there is no exact cover possible
    halt_fl = False
    for l in col_has_1_at:
        if l == []:
            print("No solution possible!")
            halt_fl = True

    row_valid = NR_OF_ROWS * [1]
    col_valid = NR_OF_COLS * [1]

    return halt_fl, row_valid, col_valid, row_has_1_at, col_has_1_at


def print_solution(solution, row_has_1_at):
    # place triominoes in matrix D 3 rows x 4 cols
    D = [[0 for i in range(4)] for j in range(3)]

    for row_number in solution:
        # print(row_number) # 1 6 14 21
        row_list = row_has_1_at[row_number]
        # print(row_list)   # 0 5 6 7
        idx = row_list[0]
        assert idx in [0, 1, 2, 3]
        symbol = ['HB', 'VB', 'L ', 'RL'][idx]
        for c in row_list[1:]:  # skip first one
            rownr = c//4-1
            colnr = c % 4
            D[rownr][colnr] = symbol
    # print('------------------------')

    for i in D:
        print(i)

    print()


def cover(r, row_valid, col_valid, row_has_1_at, col_has_1_at):
    """ Covers the cols that have a 1 in row (r) and the rows that overlap with row (r). """
    # Covers the rows.
    for i, row in enumerate(row_has_1_at):
        if any([v in r for v in row]):
            row_valid[i] = 0

    # Covers the columns.
    for c in r:
        col_valid[c] = 0

    return row_valid, col_valid


def solve(row_valid, col_valid, row_has_1_at, col_has_1_at, solution, solutions):
    """ Find a solution in the provided matrix using Algorithm X. """
    if 1 not in col_valid:
        print_solution(solution, row_has_1_at)
        return False

    # Select the column with the lowest number of 1's.
    column, occurences = 0, 100

    for i, c in enumerate(col_has_1_at):
        # Check whether the column has already been covered.
        if col_valid[i] == 0:
            continue

        # Check whether the column has the smallest number of occurences.
        if len(c) < occurences:
            column, occurences = c, len(c)

    for i in column:
        # Check if the row is uncovered.
        if row_valid[i] != 1:
            continue

        # Add the row to the solution and cover it.
        solution.append(i)

        temp_row_valid, temp_col_valid = cover(
            row_has_1_at[i], row_valid[:], col_valid[:], row_has_1_at, col_has_1_at,
        )

        # Recursive call.
        if solve(temp_row_valid, temp_col_valid, row_has_1_at, col_has_1_at, solution, solutions):
            return True

        solution.remove(i)

    # No solution was found, backtrack.
    return False


mx = make_matrix(triominoes)

halt_fl, row_valid, col_valid, row_has_1_at, col_has_1_at = prepare(mx)
if not halt_fl:
    solve(row_valid, col_valid, row_has_1_at, col_has_1_at, [], [])
