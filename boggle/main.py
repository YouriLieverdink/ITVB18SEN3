BOARD = [
    ['p', 'i', 'e', 't'],
    ['g', 'a', 'a', 't'],
    ['a', 't', 'm', 's'],
    ['h', 'u', 'i', 's'],
]


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
    prefixes = set()

    words = open('./assets/words.txt').read().split()

    for word in words:
        for i in range(len(word)):
            prefix = word[:i]

            if prefix not in prefixes:
                prefixes.add(word[:i])

    for x in range(4):
        for y in range(4):
            dfs([x, y], BOARD, '', prefixes, words, set())
