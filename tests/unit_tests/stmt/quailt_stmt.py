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
class Foo:
  def __init__(self):
    self.x = 1
  class Bar:
    def __init__(self):
        self.x = 10
        self.y = 2

class FooChild(Foo):
  def __init__(self):
    super().__init__()
    self.z = 3

f = Foo()
f.x # Quail-assert: eq 1
f2 = Foo.Bar()
f2.x # Quail-assert: eq 10
f2.y # Quail-assert: eq 2
f3 = FooChild()
f3.x # Quail-assert: eq 1
f3.z # Quail-assert: eq 3
# Quail-test:end


# Quail-test:new
"""
Name: Return
Flyable-version: v0.1a1
Description: Tests the return statement
"""
# Quail-test:start
def ret():
  return 10

ret() # Quail-assert: eq 10
# Quail-test:end


# Quail-test:new
"""
Name: Delete
Flyable-version: v0.1a1
Description: Tests the delete statement
"""
# Quail-test:start
x = 10
x # Quail-assert: eq 10
del x
if True:
  try:
    print(x)
  except:
    True # Quail-assert: eq True

lst = [1, 2, 3]
del lst[1]
lst # Quail-assert: eq [1, 3]
# Quail-test:end


# Quail-test:new
"""
Name: Assign
Flyable-version: v0.1a1
Description: Tests the assign statement
"""
# Quail-test:start
x = 10
x # Quail-assert: eq 10
x = "Hello World!"
x # Quail-assert: eq "Hello World!"
x = True
x # Quail-assert: eq True
x = 2.3
x # Quail-assert: eq 2.3
x = []
x # Quail-assert: eq []
# Quail-test:end


# Quail-test:new
"""
Name: AugAssign
Flyable-version: v0.1a1
Description: Tests the augmented assignement statement (+=)
"""
# Quail-test:start
x = 10
x # Quail-assert: eq 10
x += 5
x # Quail-assert: eq 15
x -= 5
x # Quail-assert: eq 10
# Quail-test:end


# Quail-test:new
"""
Name: AnnAssign
Flyable-version: v0.1a1
Description: Tests the annoted assignement statement
"""
# Quail-test:start
c: int
a: int = 5
a # Quail-assert: eq 5

class Test:
  def __init__(self):
      self.x: int = 5

lst: list[int] = [1, 2, 3, 4, 5]
lst # Quail-assert: eq [1, 2, 3, 4, 5]
# Quail-test:end


# Quail-test:new
"""
Name: For
Flyable-version: v0.1a1
Description: Tests the for loop definition
"""
# Quail-test:start
i = 0
for i in range(10):
  i += 1

i # Quail-assert: eq 10

lst = [1, 2, 3, 4, 5]
total = 0
for i in lst:
  total += i
total # Quail-assert: eq 15

lst2 = []
for i in "Hello":
  lst2.append(i)
lst2 # Quail-assert: eq ["H", "e", "l", "l", "o"]
# Quail-test:end


# Quail-test:new
"""
Name: AsyncFor
Flyable-version: v0.1a1
Description: Tests the async for loop definition
"""
# Quail-test:start
import asyncio
async def first():
    return 10

async def main():  
  x = 0   
  for i in range(2):
    x += await first()
  
  return x


loop = asyncio.get_event_loop()
loop.run_until_complete(main()) # Quail-assert: eq 20
# Quail-test:end


# Quail-test:new
"""
Name: While
Flyable-version: v0.1a1
Description: Tests the while loop definition
"""
# Quail-test:start
lst = [10, 20, 30, 40]
total = 0
i = 3
while i >= 0:
  total += lst[i]
  i -= 1

total # Quail-assert: eq 100
# Quail-test:end


# Quail-test:new
"""
Name: With
Flyable-version: v0.1a1
Description: Tests the with statement
"""
# Quail-test:start
class MessageWriter(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_name # Quail-assert: eq "my_file.txt"
      
    def __enter__(self):
        return "Hello World!"
  
    def __exit__(self, _a, _b, _c):
        "I'm done here" # Quail-assert: eq "I'm done here"
  
# using with statement with MessageWriter
  
with MessageWriter('my_file.txt') as xfile:
    xfile # Quail-assert: eq "Hello World!"
# Quail-test:end


# Quail-test:new
"""
Name: AsyncWith
Flyable-version: v0.1a1
Description: Tests the async with statement
"""
# Quail-test:start
import asyncio
class MessageWriter_2(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_name # Quail-assert: eq "my_file.txt"
      
    def __enter__(self):
        return "Hello World!"
  
    def __exit__(self, _a, _b, _c):
        "I'm done here" # Quail-assert: eq "I'm done here"
  
async def first_2():
    with MessageWriter_2('my_file.txt') as xfile:
        return xfile

async def main_2():  
  x = ""
  for i in range(2):
    x += await first_2()
  return x


loop = asyncio.get_event_loop()
loop.run_until_complete(main_2()) # Quail-assert: eq "Hello World!Hello World!"

# Quail-test:end


# Quail-test:new
"""
Name: Raise
Flyable-version: v0.1a1
Description: Tests the raise statement
"""
# Quail-test:start
try:
  x = 3
  raise Exception()
  x = 5
except:
  pass
  # Quail-test:end

# Quail-test:new
"""
Name: Try
Flyable-version: v0.1a1
Description: Tests the try statement
"""
# Quail-test:start

a = 1
try:
  x = 20 + "2"
  a = 2
except:
  a = 3

a # Quail-assert: eq 3

a = 1
try:
  x = 10 / 0
  a = 2
except ZeroDivisionError:
  a = 3

a # Quail-assert: eq 3

# Quail-test:end


# Quail-test:new
"""
Name: Assert
Flyable-version: v0.1a1
Description: Tests the assert statement
"""
# Quail-test:start
x = 10
assert 2 == 2
x # Quail-assert: eq 10

assert 2 != 2
# Quail-test:end


# Quail-test:new
"""
Name: Global
Flyable-version: v0.1a1
Description: Tests the global statement
No-Wrap: True
"""
# Quail-test:start
new_var = 0
def test_flyable():
  global new_var
  new_var += 5

new_var # Quail-assert: eq 0
test_flyable()
new_var # Quail-assert: eq 5
test_flyable()
new_var # Quail-assert: eq 10
test_flyable()
new_var # Quail-assert: eq 15
test_flyable()
new_var # Quail-assert: eq 20
test_flyable()
new_var # Quail-assert: eq 25
# Quail-test:end


# Quail-test:new
"""
Name: Global_Call
Flyable-version: v0.1a1
Description: Tests the global statement
No-Wrap: True
"""
# Quail-test:start

def addition(x, y):
  return x + y

x = 0
def test_flyable():
  global x
  x = addition(x, 2)
  return x

test_flyable() # Quail-assert: eq 2
test_flyable() # Quail-assert: eq 4
test_flyable() # Quail-assert: eq 6
test_flyable() # Quail-assert: eq 8
test_flyable() # Quail-assert: eq 10
# Quail-test:end


# Quail-test:new
"""
Name: NonLocal
Flyable-version: v0.1a1
Description: Tests the NonLocal statement
"""
# Quail-test:start
def test3():
  x = 5

  def test4():
    nonlocal x
    x = 10

  x # Quail-assert: eq 5
  test4()
  x # Quail-assert: eq 10
# Quail-test:end


# Quail-test:new
"""
Name: Pass
Flyable-version: v0.1a1
Description: Tests the pass statement
"""
# Quail-test:start
def test_pass():
  pass

test_pass()

for i in range(1):
  pass

if 6 == 6:
  pass

if 5 == 6:
  pass
elif 5 == 4:
  pass
else:
  pass
# Quail-test:end


# Quail-test:new
"""
Name: Break
Flyable-version: v0.1a1
Description: Tests the break statement
"""
# Quail-test:start
x = 0
for i in range(10):
  x = i
  if x == 5:
    break

x # Quail-assert: eq 5

x = 0
for i in range(5):
  pass
else:
  x = 5

x # Quail-assert: eq 5

x = 0
for i in range(5):
  break
else:
  x = 5

x # Quail-assert: eq 0
# Quail-test:end


# Quail-test:new
"""
Name: Continue
Flyable-version: v0.1a1
Description: Tests the continue statement
"""
# Quail-test:start
nb_even = 0
for i in range(10):
  if i % 2 != 0:
    continue
  nb_even += 1

nb_even # Quail-assert: eq 5
# Quail-test:end