from main import swap


def test_swap():
    # Test the functionality of the swap function.
    tour = ['h', '1', '2', '3', '4', '5', '6']

    assert swap(tour, 2, 5) == ['h', '1', '5', '4', '3', '2', '6']


if __name__ == '__main__':
    # Execute the tests.
    test_swap()

    print('All tests have passed!')
