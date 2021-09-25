from main import swap


def test_swap():
    # Test the functionality of the swap function.
    tour = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'a']

    assert swap(tour, 3, 6) == ['a', 'b', 'c', 'g', 'f', 'e', 'd', 'h', 'a']


if __name__ == '__main__':
    # Execute the tests.
    test_swap()

    print('All tests have passed!')
