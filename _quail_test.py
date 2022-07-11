def test_flyable():
    def http_error(status):
      match status:
        case 400:
          return "Bad request"
        case 404:
          return "Not found"
        case 418:
          return "I'm a teapot"
        case "useless":
          return "I'm useless"
        case x if x > 0:
          return "Here"
        case _:
          return "Else"
    
    print((http_error(400)) == ("Bad request"))
    print((http_error(404)) == ("Not found"))
    print((http_error("useless")) == ("I'm useless"))
    print((http_error(-1)) == ("Else"))
    print((http_error(1)) == ("Here"))
    print((http_error(100)) == ("Here"))

test_flyable()

test_flyable()

test_flyable()

test_flyable()

test_flyable()
