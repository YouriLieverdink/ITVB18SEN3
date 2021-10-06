from main import neighbours, parse_board


def test_parse_board():
    # Test the functionality of the parse_board function.
    board_str = """
        0 2 0
        4 1 9
        0 8 3
    """

    assert parse_board(board_str) == (
        [[0, 2, 0], [4, 1, 9], [0, 8, 3]], [1, 1]
    )


def test_neighbours():
    # Test the functionality of the neighbours function.
    assert neighbours([0, 0], 3) == [[0, 1], [1, 0]]
    assert neighbours([0, 2], 3) == [[1, 2], [0, 1]]
    assert neighbours([2, 2], 3) == [[1, 2], [2, 1]]
    assert neighbours([2, 0], 3) == [[1, 0], [2, 1]]

    assert neighbours([1, 7], 9) == [[0, 7], [1, 8], [2, 7], [1, 6]]


def main():
    # Execute the tests.
    test_parse_board()
    test_neighbours()

    print('All tests have passed.')


if __name__ == '__main__':
    main()
