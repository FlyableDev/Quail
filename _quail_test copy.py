def test_flyable():
    
    # Eq
    print((True == True) == (True))
    print((False == True) == (False))
    
    # NotEq
    print((True != False) == (True))
    print((True != True) == (False))
    
    # Lt
    print((5 < 10) == (True))
    print((5 < 5) == (False))
    print((10.2 < 5.4) == (False))
    print((10.2 < 10.2) == (False))
    
    # LtE
    print((5 <= 10) == (True))
    print((5 <= 5) == (True))
    print((10.2 <= 5.4) == (False))
    print((10.2 <= 10.2) == (True))
    
    # Gt
    print((5 > 10) == (False))
    print((5 > 5) == (False))
    print((10.2 > 5.4) == (True))
    print((10.2 > 10.2) == (False))
    
    # GtE
    print((5 >= 10) == (False))
    print((5 >= 5) == (True))
    print((10.2 >= 5.4) == (True))
    print((10.2 >= 10.2) == (True))
    
    # Is && IsNot
    x = [2, 3]
    y = [2, 3]
    print((x is x) == (True))
    print((x is not x) == (False))
    print((x is y) == (False))
    print((x is not y) == (True))
    print((True is True) == (True))
    print((True is not True) == (False))
    print((True is False) == (False))
    print((True is not False) == (True))
    
    # In
    x = [2, 3]
    y = (2, 3)
    z = {2, 3}
    a = {1: 5, 2: 5}
    print((2 in x) == (True))
    print((5 in x) == (False))
    print((2 in y) == (True))
    print((5 in y) == (False))
    print((2 in z) == (True))
    print((5 in z) == (False))
    print((2 in a) == (True))
    print((5 in a) == (False))
    
    # NotIn
    print((2 not in x) == (False))
    print((5 not in x) == (True))
    print((2 not in y) == (False))
    print((5 not in y) == (True))
    print((2 not in z) == (False))
    print((5 not in z) == (True))
    print((2 not in a) == (False))
    print((5 not in a) == (True))

test_flyable()

test_flyable()

test_flyable()

test_flyable()

test_flyable()
