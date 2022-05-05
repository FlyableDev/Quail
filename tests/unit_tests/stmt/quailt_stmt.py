"""Module stmt"""

# Quail-test:new
"""
Name: FunctionDef
Flyable-version: v0.1a1
Description: Tests the function definition
"""
# Quail-test:start
def func_no_args():
  pass

func_no_args()

def func_with_args(a: str, b: bool, c: int):
  pass

func_with_args("Hello", True, 20)

def func_with_return():
  return 2

func_with_return() # Quail-assert: eq 2

def func_with_args_and_return(x: int, y: int):
  return x + y

func_with_args_and_return(10, 20) # Quail-assert: eq 30
# Quail-test:end


# Quail-test:new
"""
Name: AsyncFuncDef
Flyable-version: v0.1a1
Description: Tests the async function definition
"""
# Quail-test:start
async def async_func():
  pass
# Quail-test:end


# Quail-test:new
"""
Name: ClassDef
Flyable-version: v0.1a1
Description: Tests the class definition
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: Return
Flyable-version: v0.1a1
Description: Tests the return statement
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: Delete
Flyable-version: v0.1a1
Description: Tests the delete statement
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: Assign
Flyable-version: v0.1a1
Description: Tests the assign statement
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: AugAssign
Flyable-version: v0.1a1
Description: Tests the augmented assignement statement (+=)
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: AnnAssign
Flyable-version: v0.1a1
Description: Tests the annoted assignement statement
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: For
Flyable-version: v0.1a1
Description: Tests the for loop definition
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: AsyncFor
Flyable-version: v0.1a1
Description: Tests the async for loop definition
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: While
Flyable-version: v0.1a1
Description: Tests the while loop definition
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: With
Flyable-version: v0.1a1
Description: Tests the with statement
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: AsyncWith
Flyable-version: v0.1a1
Description: Tests the async with statement
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: Raise
Flyable-version: v0.1a1
Description: Tests the raise statement
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: Try
Flyable-version: v0.1a1
Description: Tests the try statement
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: Assert
Flyable-version: v0.1a1
Description: Tests the assert statement
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: Import
Flyable-version: v0.1a1
Description: Tests the import statement
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: ImportFrom
Flyable-version: v0.1a1
Description: Tests the from ... import ... statement
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: Global
Flyable-version: v0.1a1
Description: Tests the global statement
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: NonLocal
Flyable-version: v0.1a1
Description: Tests the NonLocal statement
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: Expr
Flyable-version: v0.1a1
Description: Tests the Expr statement
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: Pass
Flyable-version: v0.1a1
Description: Tests the pass statement
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: Break
Flyable-version: v0.1a1
Description: Tests the break statement
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: Continue
Flyable-version: v0.1a1
Description: Tests the continue statement
"""
# Quail-test:start
# Quail-test:end