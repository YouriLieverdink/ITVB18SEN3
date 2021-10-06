from constants import BOARD


def read_file():
    # Reads the words from file and creates a set of prefixes.
    prefixes, words = set(), open('./assets/words.txt').read().split()

    # Create prefixes for all the words.
    for word in words:
        for i in range(len(word)):
            prefixes.add(word[:i])

    return (prefixes, words)


def neighbours(p, n):
    # Returns the neighbours of the provided position.
    positions = []

    # Up
    positions.append([(p[0] - 1) % n, p[1]])
    # Right
    positions.append([p[0], (p[1] + 1) % n])
    # Down
    positions.append([(p[0] + 1) % n, p[1]])
    # Left
    positions.append([p[0], (p[1] - 1) % n])

    return positions


def dfs(p, board, prefixes, word, words, visited, found):
    # Performs the deep first search algorithm to find words.
    if str(p) not in visited:
        # Continue if the item has not been visited before.
        visited.add(str(p))

        # Create a string with the current word.
        word = word + board[p[0]][p[1]]

        # Check if the word is valid.
        if word in words:
            found.add(word)

        # Continue searching when the word matches a prefix.
        if word in prefixes:
            # Search the neighbours of the current position.
            for n in neighbours(p, len(board)):
                dfs(n, board, prefixes, word, words, visited, found)

        # Remove the position when nothing matched.
        visited.remove(str(p))


if __name__ == '__main__':
    prefixes, words = read_file()
    n, found = len(BOARD), set()

    # Start the DFS algorithm from every position on the board.
    for x in range(n):
        for y in range(n):
            dfs([x, y], BOARD, prefixes, '', words, set(), found)

    print(found)
