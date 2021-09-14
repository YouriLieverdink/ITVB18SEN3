from main import is_valid, is_goal, move, next


def test_is_valid():
    # Test the functionality of the test_is_valid function.

    assert is_valid('CFGW|') == True, 'Should be True'
    assert is_valid('FG|CW') == True, 'Should be True'
    assert is_valid('CF|GW') == False, 'Should be False'
    assert is_valid('F|CGW') == False, 'Should be False'


def test_is_goal():
    # Test the functionality of the is_goal function.

    assert is_goal('CFGW|') == False, 'Should be False'
    assert is_goal('CF|GW') == False, 'Should be False'
    assert is_goal('|CFGW') == True, 'Should be True'
    assert is_goal('|GWCF') == True, 'Should be True'


def test_move():
    # Test the functionality of the move function.

    assert move('r', 'CFGW|', 'C') == 'FGW|C', 'Should be "FGW|C"'
    assert move('r', 'CF|GW', 'F') == 'C|FGW', 'Should be "C|FGW"'
    assert move('l', 'CGW|F', 'F') == 'CFGW|', 'Should be "CFGW"'
    assert move('l', '|CFGW', 'G') == 'G|CFW', 'Should be "G|CFW"'


def test_next():
    # Test the functionality of the next function.

    assert next('CFGW|') == ['CGW|F', 'GW|CF', 'CW|FG', 'CG|FW']
    assert next('F|CGW') == ['|CFGW']
    assert next('C|FGW') == ['CF|GW', 'CFG|W', 'CFW|G']


def main():
    # Execute tests
    test_is_valid()
    test_is_goal()
    test_move()
    test_next()

    print('All tests have passed.')


if __name__ == '__main__':
    main()
