from constants import BOARD


def neighbours(cursor, n):
    cursors = []

    cursors.append([(cursor[0] - 1) % n, cursor[1]])
    cursors.append([cursor[0], (cursor[1] + 1) % n])
    cursors.append([(cursor[0] + 1) % n, cursor[1]])
    cursors.append([cursor[0], (cursor[1] - 1) % n])

    return cursors


def dfs(cursor, board, word, prefixes, words, visited):

    value = board[cursor[0]][cursor[1]]

    if value in visited:
        return

    visited.add(value)
    new_word = word + value

    if new_word in words:
        print(new_word)

    if new_word in prefixes:
        # Search the neighbours
        for c in neighbours(cursor, len(board)):
            dfs(c, board, new_word, prefixes, words, visited)


if __name__ == '__main__':
    prefixes, words = set(), open('./assets/words.txt').read().split()

    for word in words:
        for i in range(len(word)):
            prefixes.add(word[:i])

    n = len(BOARD)

    for x in range(n):
        for y in range(n):
            dfs([x, y], BOARD, '', prefixes, words, set())
