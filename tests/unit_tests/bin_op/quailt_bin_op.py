"""Module where bin_op tests are created"""

# Quail-test:new
"""
Name: int_equality
Flyable-version: v0.1a1
Description: Test the equality between two integers
"""
# Quail-test:start
15 == 15 # Quail-assert: eq True
10 == 15 # Quail-assert: eq False
0 == 1 # Quail-assert: eq False
1 == -1 # Quail-assert: eq False
# Quail-test:end


# Quail-test:new
"""
Name: addition
Flyable-version: v0.1a1
Description: Test the addition operator
"""
# Quail-test:start
0 + 0  # Quail-assert: eq 0
0 + 1  # Quail-assert: eq 1
1 + 1  # Quail-assert: eq 2
from sys import maxsize

maxsize + 0  # Quail-assert: eq maxsize
0 + maxsize  # Quail-assert: eq maxsize
10000000000000 + 10000000000000   # Quail-assert: eq 20000000000000
# Quail-test:end


# Quail-test:new
"""
Name: subtraction
Flyable-version: v0.1a1
Description: Test the subtraction operator
"""
# Quail-test:start
0 - 0 # Quail-assert: eq 0
0 - 1 # Quail-assert: eq -1
1 - 0 # Quail-assert: eq 1
1 - 1 # Quail-assert: eq 0
1 - -1 # Quail-assert: eq 2
1 - +1 # Quail-assert: eq 0
-1 - -1 # Quail-assert: eq 0
-1 - +1 # Quail-assert: eq -2
+1 - +1 # Quail-assert: eq 0

51004 - 2414423 # Quail-assert: eq -2363419
# Quail-test:end


# Quail-test:new
"""
Name: multiplication
Flyable-version: v0.1a1
Description: Test the multiplication operator
"""
# Quail-test:start

0 * 0 # Quail-assert: eq 0
5 * 0 # Quail-assert: eq 0
1 * -1 # Quail-assert: eq -1
-1 * 1 # Quail-assert: eq -1
-1 * -1 # Quail-assert: eq 1
120 * 32 # Quail-assert: eq 3840
50 * -50 # Quail-assert: eq -2500
-50 * -50 # Quail-assert: eq 2500
# Quail-test:end


# Quail-test:new
"""
Name: division
Flyable-version: v0.1a1
Description: Test the divide operator
"""
# Quail-test:start
0 / 5 # Quail-assert: eq 0.0
-0 / 5 # Quail-assert: eq 0.0
1 / 10.0 # Quail-assert: eq 0.1
50 / 50 # Quail-assert: eq 1.0
50.0 / 50 # Quail-assert: eq 1.0
50 / -50 # Quail-assert: eq -1.0
-50 / -50 # Quail-assert: eq 1.0
226 / 25.3 # Quail-assert: eq 8.932806324110672

# Current fails:
1 / 10 # Quail-assert: eq 0.1
226 / 25 # Quail-assert: eq 9.04
# Quail-test:end


# Quail-test:new
"""
Name: division_by_zero
Flyable-version: v0.1a1
Description: Test the division by zero
"""
# Quail-test:start
try:
    5 / 0
except ZeroDivisionError:
    "Division by zero" # Quail-assert: eq "Division by zero"
try:
    0 / 0
except ZeroDivisionError:
    "Division by zero" # Quail-assert: eq "Division by zero"
try:
    2 % 0
except ZeroDivisionError:
    "Division by zero" # Quail-assert: eq "Division by zero"
try:
    5 // 0
except ZeroDivisionError:
    "Division by zero" # Quail-assert: eq "Division by zero"
# Quail-test:end


# Quail-test:new
"""
Name: modulo
Flyable-version: v0.1a1
Description: Test the modulo operator
"""
# Quail-test:start
0 % 2 # Quail-assert: eq 0
42 % 2 # Quail-assert: eq 0
3 % 2 # Quail-assert: eq 1
8 % 6 # Quail-assert: eq 2
-8 % -6 # Quail-assert: eq -2

# Current fails
8 % -6 # Quail-assert: eq -4
-8 % 6 # Quail-assert: eq 4
# Quail-test:end


# Quail-test:new
"""
Name: pow
Flyable-version: v0.1a1
Description: Test the pow operator
"""
# Quail-test:start
1 ** 0 # Quail-assert: eq 1
16 ** 0 # Quail-assert: eq 1
-16 ** 0 # Quail-assert: eq -1
2 ** 8 # Quail-assert: eq 256
-2 ** 8 # Quail-assert: eq -256
2 ** -8 # Quail-assert: eq 0.00390625
-2 ** -8 # Quail-assert: eq -0.00390625
# Quail-test:end


# Quail-test:new
"""
Name: floor_division
Flyable-version: v0.1a1
Description: Test the pow operator
"""
# Quail-test:start
0 // 5  # Quail-assert: eq 0
1 // 10 # Quail-assert: eq 0
1 // 10.0 # Quail-assert: eq 0.0
50 // 50 # Quail-assert: eq 1
40.0 // 50 # Quail-assert: eq 0.0
40.0 // 50.0 # Quail-assert: eq 0.0
-40 // -50 # Quail-assert: eq 0
50.0 // 12.0 # Quail-assert: eq 4.0

# Current fails:
40 // -50 # Quail-assert: eq -1
50.0 // -12.0 # Quail-assert: eq -5.0
# Quail-test:end


# Quail-test:new
"""
Name: LShift
Flyable-version: v0.1a1
Description: Test the LeftShift operator
"""
# Quail-test:start
8 << 1 # Quail-assert: eq 16
8 << 2 # Quail-assert: eq 32
8 << 4 # Quail-assert: eq 128
-3 << 1 # Quail-assert: eq -6
# Quail-test:end


# Quail-test:new
"""
Name: RShift
Flyable-version: v0.1a1
Description: Test the RightShift operator
"""
# Quail-test:start
8 >> 1 # Quail-assert: eq 4
8 << 2 # Quail-assert: eq 2
8 << 4 # Quail-assert: eq 0
-3 << 1 # Quail-assert: eq -2
# Quail-test:end


# Quail-test:new
"""
Name: BitAnd
Flyable-version: v0.1a1
Description: Test the BitAnd operator
"""
# Quail-test:start
0 & 0 # Quail-assert: eq 0
0 & 1 # Quail-assert: eq 0
1 & 0 # Quail-assert: eq 0
1 & 1 # Quail-assert: eq 1

2 & 3 # Quail-assert: eq 2
2 & 0 # Quail-assert: eq 2
-1 & -1 # Quail-assert: eq -1
12 & 3 # Quail-assert: eq 0
12 & -3 # Quail-assert: eq 12
-12 & 3 # Quail-assert: eq 0
-12 & -3 # Quail-assert: eq -12
16 & 5 # Quail-assert: eq 0
15 & 5 # Quail-assert: eq 5
# Quail-test:end


# Quail-test:new
"""
Name: BitOr
Flyable-version: v0.1a1
Description: Test the BitOr operator
"""
# Quail-test:start
0 | 0 # Quail-assert: eq 0
0 | 1 # Quail-assert: eq 1
1 | 0 # Quail-assert: eq 1
1 | 1 # Quail-assert: eq 1

2 | 3 # Quail-assert: eq 3
2 | 0 # Quail-assert: eq 2
-1 | -1 # Quail-assert: eq -1
12 | 3 # Quail-assert: eq 15
12 | -3 # Quail-assert: eq -3
-12 | 3 # Quail-assert: eq -9
-12 | -3 # Quail-assert: eq -3
# Quail-test:end


# Quail-test:new
"""
Name: BitXor
Flyable-version: v0.1a1
Description: Test the BitXor operator
"""
# Quail-test:start
0 ^ 0 # Quail-assert: eq 0
0 ^ 1 # Quail-asser: eq 1
1 ^ 0 # Quail-asser: eq 1
1 ^ 1 # Quail-asser: eq 0

156 ^ 52 # Quail-assert: eq 168
-156 ^ 52 # Quail-assert: eq -176
156 ^ -52 # Quail-assert: eq 168
-156 ^ -52 # Quail-assert: eq -176
# Quail-test:end


# Quail-test:new
"""
Name: MatMult
Flyable-version: v0.1a1
Description: Test the MatMult operator
"""
# Quail-test:start

# TODO : Add numpy to test implementation ?

# Quail-test:end