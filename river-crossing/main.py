def is_valid(state):
    # Check whether the provided state is valid.
    for s in state.split('|'):
        if ('C' in s and 'G' in s and 'F' not in s):
            return False

        if ('W' in s and 'G' in s and 'F' not in s):
            return False

    return True


def is_goal(state):
    # Check whether the provided state is the goal state.
    return state.split('|')[0] == ''


def sort_string(str):
    # Reference: https://stackoverflow.com/a/15046263/16799596
    return ''.join(sorted(str))


def move(dir, state, item):
    # Move the provided item in the provided direction.
    s = state.split('|')

    if (dir == 'r'):
        s[0] = sort_string(s[0].replace(item, ''))
        s[1] = sort_string(s[1] + item)
    else:
        s[1] = sort_string(s[1].replace(item, ''))
        s[0] = sort_string(s[0] + item)

    return '|'.join(s)


def next(state):
    # Returns the next valid and invalid states based on the provided state.
    sides = state.split('|')
    states = []

    dir = 'r' if 'F' in sides[0] else 'l'

    for item in sides[0 if dir == 'r' else 1]:
        temp = state

        if item != 'F':
            temp = move(dir, state, item)

        states.append(move(dir, temp, 'F'))

    return states


def dfs(path):
    # Performs the deep first search algorithm.
    state, paths = path[::-1][0], []

    if is_goal(state):
        return [path]

    for s in next(state):

        if is_valid(s) and s not in path:

            for p in dfs(path + [s]):
                paths = paths + [p]

    return paths


if __name__ == "__main__":
    state = 'FCGW|'

    for p in dfs([state]):
        print(p)
