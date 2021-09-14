def is_valid(state):
    for s in state.split('|'):
        if ('C' in s and 'G' in s and 'F' not in s):
            return False

        if ('W' in s and 'G' in s and 'F' not in s):
            return False

    return True


def is_goal(state):
    return len(state.split('|')[0]) == 0


def sort_string(str):
    return ''.join(sorted(str))


def move(dir, state, item):
    s = state.split('|')

    if (dir == 'r'):
        s[0] = sort_string(s[0].replace(item, ''))
        s[1] = sort_string(s[1] + item)
    else:
        s[1] = sort_string(s[1].replace(item, ''))
        s[0] = sort_string(s[0] + item)

    return '|'.join(s)


def next(state):
    sides = state.split('|')
    states = []

    dir = 'r' if 'F' in sides[0] else 'l'

    for item in sides[0 if dir == 'r' else 1]:
        temp = state

        if item != 'F':
            temp = move(dir, state, item)

        states.append(move(dir, temp, 'F'))

    return states


def forward(state, history):
    if is_goal(state):
        return print(history)

    for s in next(state):
        if is_valid(s) and s not in history:
            forward(s, history + [s])


def main():
    state = 'FCGW|'
    forward(state, [state])


if __name__ == "__main__":
    main()
