from constants import BOARD


def parse_board(value):
    # Parses the provided string and returns the board and starting cursor.
    board, temp, cursor = [], [], []

    for x, row in enumerate(value.splitlines()):
        for y, cell in enumerate(row.split()):
            temp.append(int(cell))

            if int(cell) == 1:
                cursor = [x - 1, y]

        if temp != []:
            board.append(temp)
            temp = []

    return (board, cursor)


def print_board(value, cursor):
    # Prints the board to the terminal and highlights the provided cursor.
    for x, row in enumerate(value):
        print('')

        for y, cell in enumerate(row):
            if cell < 10:
                print(' ', end='')

            if cursor == [x, y]:
                print('(' + str(cell) + ')', end='')
            else:
                print(' ' + str(cell), end=' ')

    print('\n')


def neighbours(cursor, n):
    # Returns the neigbours of the provided cursor.
    cursors = []

    # Up
    if cursor[0] - 1 >= 0:
        cursors.append([cursor[0] - 1, cursor[1]])

    # Right
    if cursor[1] + 1 < n:
        cursors.append([cursor[0], cursor[1] + 1])

    # Down
    if cursor[0] + 1 < n:
        cursors.append([cursor[0] + 1, cursor[1]])

    # Left
    if cursor[1] - 1 >= 0:
        cursors.append([cursor[0], cursor[1] - 1])

    return cursors


def dfs(cursor, board, visited, n, steps):
    # Solve the puzzle using DFS.
    value = board[cursor[0]][cursor[1]]

    # Check if we have reached the end.
    if steps == n * n:
        print_board(board, [])
        return True

    # Update the board and visited set.
    board[cursor[0]][cursor[1]] = steps
    visited.add(str(cursor))

    # Check the neighbouring cursors.
    for c in neighbours(cursor, n):
        n_value = board[c[0]][c[1]]
        # Check if the neighbour is valid.
        if n_value == 0 or n_value == steps + 1:
            if dfs(c, board, visited, n, steps + 1):
                return True

    # Undo the actions.
    board[cursor[0]][cursor[1]] = value
    visited.remove(str(cursor))

    return False


if __name__ == '__main__':
    # Start
    board, cursor = parse_board(BOARD)

    dfs(cursor, board, set(), len(board), 1)
