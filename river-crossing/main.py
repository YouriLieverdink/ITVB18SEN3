from copy import deepcopy


def is_valid(state):
    # Check whether the provided state is valid.
    for s in state.split('|'):
        # Check if cabbage and goat are together.
        if ('C' in s and 'G' in s and 'F' not in s):
            return False

        # Check if goat and wolf are together
        if ('W' in s and 'G' in s and 'F' not in s):
            return False

    return True


def is_goal(state):
    # Check whether the provided state is the goal state.
    return len(state.split('|')[0]) == 0


def move(dir, state, item):
    # Move the item in the provided state to the other side.
    s = state.split('|')

    if (dir == 'r'):
        s[0] = s[0].replace(item, '')
        s[1] = s[1] + item

        s[1] = ''.join(sorted(s[1]))
    else:
        s[1] = s[1].replace(item, '')
        s[0] = s[0] + item

        s[0] = ''.join(sorted(s[0]))

    return '|'.join(s)


def next(state):
    # Returns a list of next possible states.
    sides = state.split('|')
    states = []

    if ('F' in sides[0]):
        # The farmer is on the left.
        states.append(move('r', state, 'F'))

        for c in sides[0]:
            if c != 'F':
                new_state = move('r', state, c)
                states.append(move('r', new_state, 'F'))

    else:
        # The farmer is on the right.
        states.append(move('f', state, 'F'))

        for c in sides[1]:
            if c != 'F':
                new_state = move('l', state, c)
                states.append(move('l', new_state, 'F'))

    return states


def forward(state, history):
    # Move on step forward down the tree.

    # The base case
    if is_goal(state):
        print(history)

    states = next(state)

    # Loop through the possible states.
    for s in states:

        if is_valid(s) and s not in history:
            # Pursue this state.
            t_history = deepcopy(history)
            t_history.append(s)

            forward(s, t_history)


def main():
    # Start
    state = 'FCGW|'
    forward(state, [state])


if __name__ == "__main__":
    main()
