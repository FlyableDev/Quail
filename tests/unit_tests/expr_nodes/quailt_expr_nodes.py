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


# Quail-test:new
"""
Name: NamedExpr
Flyable-version: v0.1a1
Description: Test the named expression operator (also known as walrus operator)
"""
# Quail-test:start

# Quail-test:end