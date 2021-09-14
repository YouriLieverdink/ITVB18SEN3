from main import neighbours


def test_neighbours():
    # Test the functionality of the neighbours function.
    assert neighbours([0, 0], 4) == [
        [3, 0], [0, 1], [1, 0], [0, 3]
    ]

    assert neighbours([0, 3], 4) == [
        [3, 3], [0, 0], [1, 3], [0, 2]
    ]

    assert neighbours([3, 3], 4) == [
        [2, 3], [3, 0], [0, 3], [3, 2]
    ]

    assert neighbours([3, 0], 4) == [
        [2, 0], [3, 1], [0, 0], [3, 3]
    ]


def main():
    # Execute the tests.
    test_neighbours()

    print('All tests have passed.')


if __name__ == '__main__':
    main()
