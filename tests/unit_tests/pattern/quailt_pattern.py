"""Module pattern"""

# Quail-test:new
"""
Name: MatchValue
Flyable-version: v0.1a1
Description: Tests the value matching inside a python pattern
"""
# Quail-test:start
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

http_error(400) # Quail-assert: eq "Bad request"
http_error(404) # Quail-assert: eq "Not found"
http_error("useless") # Quail-assert: eq "I'm useless"
http_error(-1) # Quail-assert: eq "Helse"
http_error(1) # Quail-assert: eq "Here"
http_error(100) # Quail-assert: eq "Else"
# Quail-test:end


# Quail-test:new
"""
Name: MatchSingleton
Flyable-version: v0.1a1
Description: Tests the single matching inside a python pattern
"""
# Quail-test:start
def test_singleton(val):
  match val:
    case True:
      return True
    case False:
      return False
    case None:
      return None

test_singleton(True) # Quail-assert: eq True
test_singleton(False) # Quail-assert: eq False
test_singleton(None) # Quail-assert: eq None
# Quail-test:end


# Quail-test:new
"""
Name: MatchSequence
Flyable-version: v0.1a1
Description: Tests the sequence matching inside a python pattern
"""
# Quail-test:start
def test_sequence(val):
  match val:
    case [1, 2]:
      return "First"
    case (3, 4):
      return "Second"
    case {"1": 1, "2": 2}:
      return "Third"
    case (1, 2):
      return "Fourth"
    case _:
      return "Else"

test_sequence([1, 2]) # Quail-assert: eq "First"
test_sequence((1, 2)) # Quail-assert: eq "First"
test_sequence([2, 1]) # Quail-assert: eq "Else"
test_sequence([3, 4]) # Quail-assert: eq "Second"
test_sequence((3, 4)) # Quail-assert: eq "Second"
test_sequence(()) # Quail-assert: eq "Else"
test_sequence({"1": 1, "2": 2}) # Quail-assert: eq "Third"
test_sequence({"2": 2, "1": 1}) # Quail-assert: eq "Third"
test_sequence({"1": 1}) # Quail-assert: eq "Else"

# Quail-test:end


# Quail-test:new
"""
Name: MatchMapping
Flyable-version: v0.1a1
Description: Tests the mapping matching inside a python pattern
"""
# Quail-test:start

# Quail-test:end
def test_mapping(val):
  match val:
    case {"override": _}:
      return "First"
    case {"override": _, "other": _}:
      return "Second"
    case {"1": _, "2": _}:
      return "Third"
    case {**rest}:
      return "Else"

test_mapping({"override": 1}) # Quail-assert: eq "First"
test_mapping({"override": 5}) # Quail-assert: eq "First"
test_mapping({"override": 5, "other": ""}) # Quail-assert: eq "First"
test_mapping({"1": 1, "2": 2}) # Quail-assert: eq "Third"
test_mapping({"2": True, "1": "dwwd"}) # Quail-assert: eq "Third"
test_mapping({}) # Quail-assert: eq "Else"
test_mapping({"1": 1, "3": 3}) # Quail-assert: eq "Else"
test_mapping({"1": 1, "2": 2, "3": 3}) # Quail-assert: eq "Third"


# Quail-test:new
"""
Name: MatchClass
Flyable-version: v0.1a1
Description: Tests the class matching inside a python pattern
"""
# Quail-test:start
class Foo():
  def __init__(self, x, y, z = 0) -> None:
    self.x = x
    self.y = y
    self.z = z

def test_class(val):
  match val:
    case Foo(x=10, y=20):
      return "First"
    case Foo(x=50, y=0):
      return "Second"
    case Foo(x=50, y=0, z=5):
      return "Third"
    case Foo(x=50, y=10, z=5):
      return "Fourth"
    case _:
      return "Else"

test_class(Foo(10, 20)) # Quail-assert: "First"
test_class(Foo(50, 0)) # Quail-assert: "Second"
test_class(Foo(50, 0, 5)) # Quail-assert: "Second"
test_class(Foo(50, 10, 5)) # Quail-assert: "Third"
test_class(Foo(0, 0, 0)) # Quail-assert: "Else"
# Quail-test:end


# Quail-test:new
"""
Name: MatchStar
Flyable-version: v0.1a1
Description: Tests the star matching inside a python pattern
"""
# Quail-test:start
def test_star(val):
  match val:
    case [1, 2, *rest]:
      return "First"
    case [1, 2, 3, *rest]:
      return "Second"
    case [1, 3, *rest]:
      return "Third"
    case [*_]:
      return "Else sequence"
    case _:
      return "Else"

test_star([1, 2]) # Quail-assert: eq "First"
test_star([1, 2, 4]) # Quail-assert: eq "First"
test_star([1, 2, 3, 4]) # Quail-assert: eq "First"
test_star([1, 3, 4]) # Quail-assert: eq "Third"
test_star([1, 4, 3]) # Quail-assert: eq "Else sequence"
test_star([]) # Quail-assert: eq "Else sequence"
test_star(None) # Quail-assert: eq "Else"
# Quail-test:end


# Quail-test:new
"""
Name: MatchAs
Flyable-version: v0.1a1
Description: Tests the as match operator inside a python pattern
"""
# Quail-test:start
def test_as(val):
  match val:
    case [x, y]:
      return x
    case [x, y, z] as v:
      return v
    case _:
      return "Else"

test_as([0, 1]) # Quail-assert: eq 0
test_as([2, 1]) # Quail-assert: eq 2
test_as([0, 1, 2]) # Quail-assert: eq [0, 1, 2]
test_as([2, 3, 4]) # Quail-assert: eq [2, 3, 4]
# Quail-test:end


# Quail-test:new
"""
Name: MatchOr
Flyable-version: v0.1a1
Description: Tests the or match operator inside a python pattern
"""
# Quail-test:start
def test_or(val):
  match val:
    case [4] | 5:
      return "First"
    case ([*rest]) | ([1, 2, 3, *rest]):
      return "Second"
    case _:
      return "Else"

test_or([4]) # Quail-assert: eq "First"
test_or(5) # Quail-assert: eq "First"
test_or([1]) # Quail-assert: eq "Second"
test_or([1, 2, 3, 4 ,5]) # Quail-assert: eq "Second"
test_or(10) # Quail-assert: eq "Else"
# Quail-test:end