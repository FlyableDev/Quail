def test_flyable():
    print(("Hello World!"[:5] == "Hello") == True)
    print(("Hello World!"[6:] == "World!") == True)
    print(("Hello World!"[:] == "Hello World!") == True)
    print(("Hello World!"[0:0] == "") == True)
    print(("Hello World!"[2:4] == "ll") == True)
    print(("Hello World!"[:-7] == "Hello") == True)
    print(("Hello World!"[-6:] == "World!") == True)
    print(("Hello World!"[-6:-5] == "W") == True)
    

test_flyable()

test_flyable()

test_flyable()

test_flyable()

test_flyable()
