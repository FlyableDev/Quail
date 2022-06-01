"""Module list"""

# Quail-test:new
"""
Name: empty_list
Flyable-version: v0.1a1
Dependencies: binop 
Description: YOUR_DESCRIPTION
"""
# Quail-test:start
def test():
    num1 = 8
    num2 = -3
    num1 % num2  # Q-assert: eq -1

test()

# Quail-test:end

# Quail-test:new
"""
Name: list_len
Flyable-version: v0.1a1
Description: tests list len
"""
# Quail-test:start
x = [1, 2, 3]
len(x) # Quail-assert: eq 3
x = []
x # Quail-assert: eq 0
# Quail-test:end
# Quail-test:new
"""
Name: compile_list
Flyable-version: v0.1a1
Description: tests compile list
"""
# Quail-test:start

# Quail-test:end
