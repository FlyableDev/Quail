"""Module expr_nodes"""

# Quail-test:new
"""
Name: BoolOp
Flyable-version: v0.1a1
Description: Test boolean node expression (and and or operators)
"""
# Quail-test:start
True and True  # Quail-assert: eq True
True and False  # Quail-assert: eq False
False and True  # Quail-assert: eq False
False and False  # Quail-assert: eq False

1 and 1  # Quail-assert: eq True
1 and 0  # Quail-assert: eq False
0 and 1  # Quail-assert: eq False
0 and 0  # Quail-assert: eq False

True or True  # Quail-assert: eq True
True or False  # Quail-assert: eq True
False or True  # Quail-assert: eq True
False or False  # Quail-assert: eq False

1 or 1  # Quail-assert: eq True
1 or 0  # Quail-assert: eq True
0 or 1  # Quail-assert: eq True
0 or 0  # Quail-assert: eq False
# Quail-test:end

# Quail-test:new
"""
Name: NamedExpr
Flyable-version: v0.1a1
Description: Test the named expression operator (also known as walrus operator)
"""
# Quail-test:start
print(walrus := True)
walrus  # Quail-assert: eq True

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

not True  # Quail-assert: eq False
not False  # Quail-assert: eq True
not 1  # Quail-assert: eq False
not 0  # Quail-assert: eq True

~True  # Quail-assert: eq -2
~False  # Quail-assert: eq -1
~1  # Quail-assert: eq -2
~0  # Quail-assert: eq -1
~-20  # Quail-assert: eq 19
# Quail-test:end


# Quail-test:new
"""
Name: Lambda
Flyable-version: v0.1a1
Description: Test the lambda expressions
"""
# Quail-test:start
isTrue = lambda x: x == True
isTrue(True)  # Quail-assert: eq True
isTrue(9)  # Quail-assert: eq False

raise_to_power = lambda x, y: x ** y
raise_to_power(2, 3)  # Quail-assert: eq 8
# Quail-test:end


# Quail-test:new
"""
Name: Dict
Flyable-version: v0.1a1
Description: Test the dictionnary creation and unpacking
"""
# Quail-test:start
my_dict = dict()
my_dict  # Quail-assert: eq {}

my_dict = {}
my_dict  # Quail-assert: eq {}

my_dict = {"test": 1, 2: "True", 4.5: True, False: []}
my_dict  # Quail-assert: eq {'test': 1, 2: 'True', 4.5: True, False: []}

my_dict.clear()
my_dict # Quail-assert: eq {}

person = {
    "name": "Albert",
    "age": 40,
    "lastName": "Smith"
}
person['name']  # Quail-assert: eq "Albert"
person.get('name')  # Quail-assert: eq "Albert"
'name' in person  # Quail-assert: eq True
'birth' in person  # Quail-assert: eq False
vals = ['name', 'age', 'lastName']
i = 0
for key in person.keys():
    key # Quail-assert: eq vals[i]
    i += 1
vals = ['Albert', 40, 'Smith']
i = 0
for val in person.values():
    val # Quail-assert: eq vals[i]
    i += 1
person.pop("name")  # Quail-assert: eq "Albert"
person  # Quail-assert: eq {'age': 40, 'lastName': 'Smith'}
person.popitem()  # Quail-assert: eq ('lastName', 'Smith')
person # Quail-assert: eq {'age': 40}
person.setdefault("birth", 2000)
person['birth']  # Quail-assert: eq 2000
person.update()

person = {
    "name": "Albert",
    "lastName": "Smith",
    "age": 40
}
person.popitem()  # Quail-assert: eq ('age', 40)

regions = my_dict.fromkeys({"Canada", "USA"}, "Country")
regions  # Quail-assert: eq {'USA': 'Country', 'Canada': 'Country'}

regions = {}
regions["Canada"] = "Country"
regions["USA"] = "Country"
regions["Europe"] = "Continent"
vals = [('Canada', 'Country'), ('USA', 'Country'), ('Europe', 'Continent')]
i = 0
for key, val in regions.items():
    key == vals[i][0] # Quail-assert: eq True
    val == vals[i][1] # Quail-assert: eq True
    i += 1

d1 = {1: 10, 2: 20}
d2 = {3: 30, 4: 40}

d1.update(d2)
d1  # Quail-assert: eq {1: 10, 2: 20, 3: 30, 4: 40}
d2  # Quail-assert: eq {3: 30, 4: 40}

len(d1)  # Quail-assert: eq 4
len({})  # Quail-assert: eq 0

# Quail-test:end


# Quail-test:new
"""
Name: Set
Flyable-version: v0.1a1
Description: Test the python set
"""
# Quail-test:start
set1 = set()
set1  # Quail-assert: eq set()
set1 = {1}
set1  # Quail-assert: eq {1}
set1.add(2)
set1.add(2)
set1  # Quail-assert: eq {1, 2}
set1.clear()
set1  # Quail-assert: eq set()
set1 = {2, 2, 3}
set1.discard(2)
set1  # Quail-assert: eq {3}
# Discarding non-existing element
set1.discard(10)
set1  # Quail-assert: eq {3}
set1.clear()
set1 = {1, 2, 3, 4}
set1.intersection({2, 3, 5})  # Quail-assert: eq {2, 3}
set1.intersection_update({2})
set1  # Quail-assert: eq {2}
set1 = {1, 2, 3}
set1.difference({1, 3, 5})  # Quail-assert: eq {2}
set1.difference_update({1, 3, 5})
set1  # Quail-assert: eq {2}
set1 = {1, 2, 3}
set1.isdisjoint({0, 4, 5})  # Quail-assert: eq True
set1.isdisjoint({0, 2, 4})  # Quail-assert: eq False
set1.issubset({0, 2, 1, 3, 4})  # Quail-assert: eq True
set1.issubset({0, 1, 2})  # Quail-assert: eq False
set1.issuperset({1, 2})  # Quail-assert: eq True
set1.issuperset({})  # Quail-assert: eq True
set1.issuperset({3, 4})  # Quail-assert: eq False
set1.pop()  # Quail-assert: eq 1
set1  # Quail-assert: eq {2, 3}
set1 = {1, 2, 3}
set1.symmetric_difference({1, 4, 5})  # Quail-assert: eq {2, 3, 4, 5}
set1.symmetric_difference({})  # Quail-assert: eq set1
set1.symmetric_difference_update({1, 4, 5})
set1  # Quail-assert: eq {2, 3, 4, 5}
set1 = {1, 2, 3}
set1.union({1, 3, 4, 5, 6})  # Quail-assert: eq {1, 2, 3, 4, 5, 6}
set1.update({1, 3, 4, 5, 6})
set1  # Quail-assert: eq {1, 2, 3, 4, 5, 6}
# Quail-test:end


# Quail-test:new
"""
Name: ListComp
Flyable-version: v0.1a1
Description: Test the lists comprehension
"""
# Quail-test:start
vec = [-4, -2, 0, 2, 4]

# Doubling elements
[x * 2 for x in vec]  # Quail-assert: eq [-8, -4, 0, 4, 8]
# Filter positive elements
[x for x in vec if x >= 0]  # Quail-assert: eq [0, 2, 4]
# Convert every number to positive
[x if x >= 0 else -x for x in vec]  # Quail-assert: eq [4, 2, 0, 2, 4]
# Flattening list
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[num for elem in vec for num in elem]  # Quail-assert: eq [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Quail-test:end


# Quail-test:new
"""
Name: SetComp
Flyable-version: v0.1a1
Description: Test the set comprehension
"""
# Quail-test:start
{2 for i in range(20)}  # Quail-assert: eq {2}
{(i, j) for j in range(4, 7) for i in range(6, 8)}  # Quail-assert: eq {(7, 4), (6, 5), (6, 4), (7, 6), (6, 6), (7, 5)}
# Quail-test:end


# Quail-test:new
"""
Name: DictComp
Flyable-version: v0.1a1
Description: Test the dict comprehension
"""
# Quail-test:start
vec = [1, 2, 3, 4]
{i: i + 2 for i in vec}  # Quail-assert: eq {1: 3, 2: 4, 3: 5, 4: 6}
{i % 2: i for i in vec}  # Quail-assert: eq {1: 3, 0: 4}
# Double each value in the dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
{k: v * 2 for (k, v) in my_dict.items()}  # Quail-assert: eq {'a': 2, 'b': 4, 'c': 6, 'd': 8, 'e': 10}
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
{n: n ** 2 for n in numbers if n % 2 == 0}  # Quail-assert: eq {0: 0, 8: 64, 2: 4, 4: 16, 6: 36}
# Quail-test:end


# Quail-test:new
"""
Name: GeneratorExp
Flyable-version: v0.1a1
Description: Test the named expression operator (also known as walrus operator)
"""
# Quail-test:start
even_squares = (x * x for x in range(10) if x % 2 == 0)
[i for i in even_squares] # Quail-assert: eq [0, 4, 16, 36, 64]
# Quail-test:end


# Quail-test:new
"""
Name: Await
Flyable-version: v0.1a1
Description: Test the await expression
"""
# Quail-test:start
import asyncio

async def functionality():
    return True

async def test_functionality():
    return await functionality()

loop = asyncio.get_event_loop()
coroutine = test_functionality()
loop.run_until_complete(coroutine) # Quail-assert: eq True

async def print_B(): #Simple async def
    return 2

async def main_def():
    return await asyncio.gather(print_B())
asyncio.run(main_def()) # Quail-assert: eq [2]
# Quail-test:end


# Quail-test:new
"""
Name: Yield
Flyable-version: v0.1a1
Description: Test the yield expression
"""
# Quail-test:start
# A simple generator function
def my_gen():
    """A generator that fakes a read from a file, socket, etc."""
    for i in range(4):
        yield i + 1

a = my_gen()
next(a) # Quail-assert: eq 1
next(a) # Quail-assert: eq 2
next(a) # Quail-assert: eq 3
next(a) # Quail-assert: eq 4
a = my_gen()
next(a) # Quail-assert: eq 1
# Quail-test:end


# Quail-test:new
"""
Name: YieldFrom
Flyable-version: v0.1a1
Description: Test the YieldFrom expression
"""
# Quail-test:start
def reader():
    """A generator that fakes a read from a file, socket, etc."""
    for i in range(4):
        yield i + 1

def reader_wrapper(g):
    yield from g

wrap = reader_wrapper(reader())
next(wrap) # Quail-assert: eq 1
next(wrap) # Quail-assert: eq 2
next(wrap) # Quail-assert: eq 3
next(wrap) # Quail-assert: eq 4
# Quail-test:end


# Quail-test:new
"""
Name: Compare
Flyable-version: v0.1a1
Description: Test the compare expression
"""
# Quail-test:start

# Eq
True == True # Quail-assert: eq True
False == True # Quail-assert: eq False

# NotEq
True != False # Quail-assert: eq True
True != True # Quail-assert: eq False

# Lt
5 < 10 # Quail-assert: eq True
5 < 5 # Quail-assert: eq False
10.2 < 5.4 # Quail-assert: eq False
10.2 < 10.2 # Quail-assert: eq False

# LtE
5 <= 10 # Quail-assert: eq True
5 <= 5 # Quail-assert: eq True
10.2 <= 5.4 # Quail-assert: eq False
10.2 <= 10.2 # Quail-assert: eq True

# Gt
5 > 10 # Quail-assert: eq False
5 > 5 # Quail-assert: eq False
10.2 > 5.4 # Quail-assert: eq True
10.2 > 10.2 # Quail-assert: eq False

# GtE
5 >= 10 # Quail-assert: eq False
5 >= 5 # Quail-assert: eq True
10.2 >= 5.4 # Quail-assert: eq True
10.2 >= 10.2 # Quail-assert: eq True

# Is && IsNot
x = [2, 3]
y = [2, 3]
x is x # Quail-assert: eq True
x is not x # Quail-assert: eq False
x is y # Quail-assert: eq False
x is not y # Quail-assert: eq True
True is True # Quail-assert: eq True
True is not True # Quail-assert: eq False
True is False # Quail-assert: eq False
True is not False # Quail-assert: eq True

# In
x = [2, 3]
y = (2, 3)
z = {2, 3}
a = {1: 5, 2: 5}
2 in x # Quail-assert: eq True
5 in x # Quail-assert: eq False
2 in y # Quail-assert: eq True
5 in y # Quail-assert: eq False
2 in z # Quail-assert: eq True
5 in z # Quail-assert: eq False
2 in a # Quail-assert: eq True
5 in a # Quail-assert: eq False

# NotIn
2 not in x # Quail-assert: eq False
5 not in x # Quail-assert: eq True
2 not in y # Quail-assert: eq False
5 not in y # Quail-assert: eq True
2 not in z # Quail-assert: eq False
5 not in z # Quail-assert: eq True
2 not in a # Quail-assert: eq False
5 not in a # Quail-assert: eq True
# Quail-test:end


# Quail-test:new
"""
Name: Call
Flyable-version: v0.1a1
Description: Test the call expression (function call)
"""
# Quail-test:start
class Foo:
    def __str__(self) -> str:
        return "Hey!"

def foo():
    return True

foo() # Quail-assert: eq True

bar = Foo()
str(bar) # Quail-assert: eq "Hey!"
# Quail-test:end


# Quail-test:new
"""
Name: FormattedValue
Flyable-version: v0.1a1
Description: Test the FormattedValue expression (formats a value to a certain formatting)
"""
# Quail-test:start
"{}, {} and {}".format('John','Bill','Sean') # Quail-assert: eq "John, Bill and Sean"
"{1}, {0} and {2}".format('John','Bill','Sean') # Quail-assert: eq "Bill, John and Sean"
"{s}, {b} and {j}".format(j='John',b='Bill',s='Sean') # Quail-assert: eq "Sean, Bill and John"
# Quail-test:end


# Quail-test:new
"""
Name: JoinedStr
Flyable-version: v0.1a1
Description: Test the JoinedStr expression (Joining strings together)
"""
# Quail-test:start
name = "Bob"
a = 95.2424242424
f"This is a test {(a * 2):.5}. Some more text {name}" # Quail-assert: eq "This is a test 190.48. Some more text Bob"
f"Another test" # Quail-assert: eq "Another test"
f"" # Quail-assert: eq ""
# Quail-test:end


# Quail-test:new
"""
Name: Constant
Flyable-version: v0.1a1
Description: Test the constant expression (constant number, string, None, tuples, frozensets)
"""
# Quail-test:start
PI = 3.14
PI # Quail-assert: eq 3.14

GRAVITY = 9.8
GRAVITY # Quail-assert: eq 9.8

# Quail-test:end


# Quail-test:new
"""
Name: Attribute
Flyable-version: v0.1a1
Description: Test the Attribute expression (access to an attribute with the following ctx options: Load, Store or Del)
"""
# Quail-test:start
x = 5
class Foo2:
    x = 2

    def bar(self):
        return "Hey! " + str(self.x)

foo2 = Foo2()
foo2.bar() # Quail-assert: eq "Hey! 2"
foo2.x = 10
foo2.bar() # Quail-assert: eq "Hey! 10"

# Quail-test:end


# Quail-test:new
"""
Name: Subscript
Flyable-version: v0.1a1
Description: Test the subscript expression (subscripts an object, for example slicing of lists and tuples)
"""
# Quail-test:start
x = [2, 3]
y = (2, 3)
z = {0: 5, 3: 5}
x[0] # Quail-assert: eq 2
y[0] # Quail-assert: eq 2
z[0] # Quail-assert: eq 5
# Quail-test:end


# Quail-test:new
"""
Name: Starred
Flyable-version: v0.1a1
Description: Test the Starred expression (Access to a *var variable reference)
"""
# Quail-test:start
def starred(*args):
    return args

starred(1, 2, 3, 4, 5) # Quail-assert: eq (1, 2, 3, 4, 5)
starred() # Quail-assert: eq ()

def starred2(**kwargs):
    return kwargs

starred2(x=2, y=2) # Quail-assert: eq {"x": 2, "y": 2}
starred2() # Quail-assert: eq {}
# Quail-test:end


# Quail-test:new
"""
Name: Name
Flyable-version: v0.1a1
Description: Test the name expression (variable name as a string with a the following ctx options: Load, Store, Del)
"""
# Quail-test:start
x = 2
x # Quail-assert: eq 2
del x

x = 0
def scope1():
    x = 1
    x # Quail-assert: eq 1

    def scope2():
        return x
    
    scope2() # Quail-assert: eq 1
    
    def scope3():
        x = 3
        x # Quail-assert: eq 3
        return x

    scope3() # Quail-assert: eq 3
    scope2() # Quail-assert: eq 1
    x = 5
    scope2() # Quail-assert: eq 5
    scope3() # Quail-assert: eq 3

    return x
scope1() # Quail-assert: eq 5
x # Quail-assert: eq 0
# Quail-test:end


# Quail-test:new
"""
Name: List
Flyable-version: v0.1a1
Description: Test the List expression
"""
# Quail-test:start
lst = [1, 2, 1]
lst[1] # Quail-assert: eq 2
lst.count(1) # Quail-assert: eq 2
len(lst) # Quail-assert: eq 3
lst.append(5)
len(lst) # Quail-assert: eq 4
lst[len(lst) - 1] # Quail-assert: eq 5
# Quail-test:end


# Quail-test:new
"""
Name: Tuple
Flyable-version: v0.1a1
Description: Test the tuple expression
"""
# Quail-test:start
tple = (2,)
tple # Quail-assert: eq (2,)
tple = (2, 3)
tple[0] # Quail-assert: eq 2
x, y = tple
x # Quail-assert: eq 2
y # Quail-assert: eq 3
# Quail-test:end


# Quail-test:new
"""
Name: Slice
Flyable-version: v0.1a1
Description: Test the slice expression (subscript of an object from a value to another)
"""
# Quail-test:start
lst = [i for i in range(10)]
lst[0:10:2] # Quail-assert: eq [0, 2, 4, 6, 8]
slc = slice(0, 10, 2)
lst[slc] # Quail-assert: eq [0, 2, 4, 6, 8]
lst[:-2] # Quail-assert: eq [0, 1, 2, 3, 4, 5, 6, 7]
lst[-2:] # Quail-assert: eq [8, 9]
lst[-2:9] # Quail-assert: eq [8]
lst[::-1] # Quail-assert: eq [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# Quail-test:end
