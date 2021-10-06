from intersect import Point, on_segment, orientation, do_intersect


def test_on_segment() -> None:
    # Test the functionality of the on_segment function.
    p1, p2 = Point(-3, -3, ''), Point(1, 1, '')

    q = Point(0, 0, '')
    assert on_segment(p1, p2, q) == True

    q = Point(-2, 1, '')
    assert on_segment(p1, p2, q) == False


def test_orientation() -> None:
    # Test the functionality of the orientation function.
    p1, p2 = Point(-3, -3, ''), Point(1, 1, '')

    q1 = Point(2, 2, '')
    assert orientation(p1, p2, q1) == 0

    q2 = Point(3, -1, '')
    assert orientation(p1, p2, q2) == 1

    q3 = Point(-3, 2, '')
    assert orientation(p1, p2, q3) == 2


def test_do_intersect() -> None:
    # Test the functionality of the do_intersect function.
    p1, p2 = Point(-3, -3, ''), Point(1, 1, '')

    q1, q2 = Point(-3, 2, ''), Point(1, -2, '')
    assert do_intersect(p1, p2, q1, q2) == True

    q1, q2 = Point(2, 2, ''), Point(4, 4, '')
    assert do_intersect(p1, p2, q1, q2) == False

    q1, q2 = Point(-1, -1, ''), Point(3, 3, '')
    assert do_intersect(p1, p2, q1, q2) == True

    q1, q2 = Point(3, 0, ''), Point(6, 0, '')
    assert do_intersect(p1, p2, q1, q2) == False

    p1, p2 = Point(563, 485, ''), Point(641, 591, '')
    q1, q2 = Point(618, 483, ''), Point(67, 615, '')

    assert do_intersect(p1, p2, q1, q2) == True


if __name__ == '__main__':
    # Execute the tests.
    test_on_segment()
    test_orientation()
    test_do_intersect()

    print('All tests have passed!')
