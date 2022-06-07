"""Module where equality body tests are created"""

# Quail-test:new
"""
Name: int_equality
Flyable-version: v0.1a1
Description: Test the equality between two integers
"""
# Quail-test:start
15 == 15  # Quail-assert: eq True
# Quail-test:end


# Quail-test:new
"""
Name: float_equality
Flyable-version: v0.1a1
Description: Test the equality between two floats
"""
# Quail-test:start
15.12 == 15.12 # Quail-assert: eq True
# Quail-test:end


# Quail-test:new
"""
Name: bool_equality
Flyable-version: v0.1a1
Description: Test the equality between two boolean
Dependencies: subtraction, division
"""
# Quail-test:start
False == False  # Quail-assert: eq True
True == True    # Quail-assert: eq True
False == True   # Quail-assert: eq False
True == False   # Quail-assert: eq False
# Quail-test:end


# Quail-test:new
"""
Name: triple_equality
Flyable-version: v0.1a1
Description: Test triple equality
"""
# Quail-test:start
2 == 2 == 2  # Quail-assert: eq True
# Quail-test:end


# Quail-test:new
"""
Name: is_operator
Flyable-version: v0.1a1
Description: Test the is operator
"""
# Quail-test:start
True is True   # Quail-assert: eq True
True is False  # Quail-assert: eq False
False is False # Quail-assert: eq True
False is True  # Quail-assert: eq False
# Quail-test:end


# Quail-test:new
"""
Name: zero_and_one_bool_comparison_with_is
Flyable-version: v0.1a1
Description: Test the equality between 0, 1 and booleans using is operator
"""
# Quail-test:start
0 is False # Quail-assert: eq False
1 is False # Quail-assert: eq False
0 is True  # Quail-assert: eq False
1 is True  # Quail-assert: eq False
# Quail-test:end


# Quail-test:new
"""
Name: zero_and_one_bool_comparison_with_equal
Flyable-version: v0.1a1
Description: Test the equality between 0, 1 and boolean using equal operator
"""
# Quail-test:start
0 == False # Quail-assert: eq True
1 == False # Quail-assert: eq False
0 == True # Quail-assert: eq False
1 == True # Quail-assert: eq True
# Quail-test:end
