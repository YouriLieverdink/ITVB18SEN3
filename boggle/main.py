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


def dfs(cursor, board, word, prefixes, words):

    value = word + board[cursor[0]][cursor[1]]

    if value in words:
        print(value)

    if value in prefixes:
        # Search the neighbours
        for c in neighbours(cursor, len(board)):
            dfs(c, board, value, prefixes, words)


def main():
    prefixes = set()

    words = open('./assets/words.txt').read().split()

    for word in words:
        for i in range(len(word)):
            prefixes.add(word[:i])

    for x in range(4):
        for y in range(4):
            dfs([x, y], BOARD, '', prefixes, words)


if __name__ == '__main__':
    main()
