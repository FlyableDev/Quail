"""Module binop"""

# Quail-test:new
"""
Name: add_int_on_int
Flyable-version: v0.1a1
Description: tests the add binop for two ints
"""
# Quail-test:start
def test():
    1 + 1  # Q-assert: eq 2
    1 + -1  # Q-assert: eq 0


test()
# Quail-test:end
