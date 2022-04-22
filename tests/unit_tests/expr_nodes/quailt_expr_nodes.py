"""Module expr_nodes"""

# Quail-test:new
"""
Name: BoolOp
Flyable-version: v0.1a1
Description: Test boolean node expression (and and or operators)
"""
# Quail-test:start
True and True  # Quail-assert: True
True and False  # Quail-assert: False
False and True  # Quail-assert: False
False and False  # Quail-assert: False

1 and 1  # Quail-assert: True
1 and 0  # Quail-assert: False
0 and 1  # Quail-assert: False
0 and 0  # Quail-assert: False

True or True  # Quail-assert: True
True or False  # Quail-assert: True
False or True  # Quail-assert: True
False or False  # Quail-assert: False

1 or 1  # Quail-assert: True
1 or 0  # Quail-assert: True
0 or 1  # Quail-assert: True
0 or 0  # Quail-assert: False
# Quail-test:end

# Quail-test:new
"""
Name: NamedExpr
Flyable-version: v0.1a1
Description: Test the named expression operator (also known as walrus operator)
"""
# Quail-test:start
print(walrus := True)
walrus # Quail-assert: True

# TODO: Add more walrus tests

# Quail-test:end


# Quail-test:new
"""
Name: UnaryOp
Flyable-version: v0.1a1
Description: Test the UnaryOp (UAdd, USub, Not, Invert)
"""
# Quail-test:start

# TODO: UAdd operator
# TODO: USub operator

not True # Quail-assert: False
not False # Quail-assert: True
not 1 # Quail-assert: False
not 0 # Quail-assert: True

~True # Quail-assert: -2
~False # Quail-assert: -1
~1 # Quail-assert : -2
~0 # Quail-assert : -1
~-20 # Quail-assert : 19
# Quail-test:end


# Quail-test:new
"""
Name: Lambda
Flyable-version: v0.1a1
Description: Test the lambda expressions
"""
# Quail-test:start
isTrue = lambda x: x == True
isTrue(6) # Quail-assert: True
isTrue(9) # Quail-assert: False

raise_to_power = lambda x, y: x ** y
raise_to_power(2, 3) # Quail-assert: 8
# Quail-test:end


# Quail-test:new
"""
Name: Dict
Flyable-version: v0.1a1
Description: Test the dictionnary creation and unpacking
"""
# Quail-test:start
person = {
  "name": "Albert",
  "age": 40,
  "siblings": [
    "romane",
    "sophia",
    "robert"
  ]
}
# Quail-test:end


# Quail-test:new
"""
Name: Set
Flyable-version: v0.1a1
Description: Test the python set
"""
# Quail-test:start
set1 = set()
set1 # Quail-assert: eq {}
set1 = {1}
set1 # Quail-assert: eq {}
set1.add(2)
set1.add(2)
set1 # Quail-assert: eq {1, 2}
set1.clear()
set1 # Quail-assert: eq {}
set1 = {2, 2, 3}
set1.discard(2)
set1 # Quail-assert: eq {3}
# Discarding non-existing element
set1.discard(10)
set1 # Quail-assert: eq {3}
set1.clear()
set1 = {1, 2, 3, 4}
set1.intersection({2, 3, 5}) # Quail-assert: eq {2, 3}
set1.intersection_update({2})
set1 # Quail-assert: eq {2}
set1 = {1, 2, 3}
set1.difference({0, 1, 2, 3, 4}) # Quail-assert: eq {0, 4}
set1.difference_update({ 0, 1, 2, 3, 4})
set1 # Quail-assert: eq {0, 4}
set1 = {1, 2, 3}
set1.isdisjoint({0, 4, 5}) # Quail-assert: eq True
set1.isdisjoint({0, 2, 4}) # Quail-assert: eq False
set1.issubset({0, 2, 1, 3, 4}) # Quail-assert: eq True
set1.issubset({0, 1, 2}) # Quail-assert: eq False
set1.issuperset({1, 2}) # Quail-assert: eq True
set1.issuperset({}) # Quail-assert: eq True
set1.issuperset({3, 4}) # Quail-assert: eq False
set1.pop() # Quail-assert: eq 3
set1 # Quail-assert: eq {2, 3}
set1 = {1, 2, 3}
set1.symmetric_difference({1, 4, 5}) # Quail-assert: eq {2, 3, 4, 5}
set1.symmetric_difference({}) # Quail-assert: eq set1
set1.symmetric_difference_update({1, 4, 5})
set1 # Quail-assert: eq {2, 3, 4, 5}
set1 = {1, 2, 3}
set1.union({1, 3, 4, 5, 6}) # Quail-assert: eq {1, 2, 3, 4, 5, 6}
set1.update({1, 3, 4, 5, 6})
set1 # Quail-assert: eq {1, 2, 3, 4, 5, 6}
# Quail-test:end


# Quail-test:new
"""
Name: NamedExpr
Flyable-version: v0.1a1
Description: Test the named expression operator (also known as walrus operator)
"""
# Quail-test:start

# Quail-test:end


# Quail-test:new
"""
Name: NamedExpr
Flyable-version: v0.1a1
Description: Test the named expression operator (also known as walrus operator)
"""
# Quail-test:start

# Quail-test:end