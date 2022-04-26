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
walrus # Quail-assert: eq True

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

not True # Quail-assert: eq False
not False # Quail-assert: eq True
not 1 # Quail-assert: eq False
not 0 # Quail-assert: eq True

~True # Quail-assert: eq -2
~False # Quail-assert: eq -1
~1 # Quail-assert: eq -2
~0 # Quail-assert: eq -1
~-20 # Quail-assert: eq 19
# Quail-test:end


# Quail-test:new
"""
Name: Lambda
Flyable-version: v0.1a1
Description: Test the lambda expressions
"""
# Quail-test:start
isTrue = lambda x: x == True
isTrue(6) # Quail-assert: eq True
isTrue(9) # Quail-assert: eq False

raise_to_power = lambda x, y: x ** y
raise_to_power(2, 3) # Quail-assert: eq 8
# Quail-test:end


# Quail-test:new
"""
Name: Dict
Flyable-version: v0.1a1
Description: Test the dictionnary creation and unpacking
"""
# Quail-test:start
dict = dict()
dict # Quail-assert: eq {}

dict = {}
dict # Quail-assert: eq {}

dict = {"test": 1, 2: "True", 4.5: True, False: []}
dict # Quail-assert: eq {'test': 1, 2: 'True', 4.5: True, False: []}

dict.clear() # Quail-assert: eq {}

person = {
  "name": "Albert",
  "age": 40,
  "lastName": "Smith"
}
person['name'] # Quail-assert: eq "Albert"
person.get('name') # Quail-assert: eq "Albert"
'name' in person # Quail-assert: eq True
'birth' in person # Quail-assert: eq False
person.keys() # Quail-assert: eq dict_keys(['name', 'age'])
person.values() # Quail-assert: eq dict_values(['Albert', 40])
person.pop("name") # Quail-assert: eq "Albert"
person # Quail-assert: eq {'age': 40, 'lastName': 'Smith'}
person.popitem() # Quail-assert: eq ('lastName', 'Smith')
person # Quail-assert: eq {'lastName': 'Smith'}
person.setdefault("birth", "2000")
person['birth'] # Quail-assert: eq "2000"
person.update()

person = {
  "name": "Albert",
  "lastName": "Smith",
  "age": 40
}
person.popitem() # Quail-assert: eq ('age', 41)

regions = dict.fromkeys({ "Canada", "USA"}, "Country") 
regions # Quail-assert: eq {'USA': 'Country', 'Canada': 'Country'}
x = regions.items() # Quail-assert: eq []
regions["Europe"] = "Continent"
x # Quail-assert: eq dict_items([('USA', 'Country'), ('Canada', 'Country'), ('Europe', 'Continent')])

d1 = {1: 10, 2: 20}
d2 = {3: 30, 4: 40}

d1.update(d2)
d1 # Quail-assert: eq {1: 10, 2: 20, 3: 30, 4: 40}
d2 # Quail-assert: eq {3: 30, 4: 40}

len(d1) # Quail-assert: eq: 4
len({}) # Quail-assert: eq: 0

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
Name: ListComp
Flyable-version: v0.1a1
Description: Test the lists comprehension
"""
# Quail-test:start
vec = [-4, -2, 0, 2, 4]

# Doubling elements
[x*2 for x in vec] # Quail-assert: eq [-8, -4, 0, 4, 8]
# Filter positive elements
[x for x in vec if x >= 0] # Quail-assert: eq [0, 2, 4]
# Convert every number to positive
[x if x >= 0 else -x for x in vec] # Quail-assert: eq [4, 2, 0, 2, 4]
# Flattening list
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem] # Quail-assert: eq [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Quail-test:end


# Quail-test:new
"""
Name: SetComp
Flyable-version: v0.1a1
Description: Test the set comprehension
"""
# Quail-test:start
{2 for i in range(20)} # Quail-assert: eq {2}
{{i,j} for j in range(4,7) for i in range(6,8)} # Quail-assert: eq {(7, 4), (6, 5), (6, 4), (7, 6), (6, 6), (7, 5)}
# Quail-test:end


# Quail-test:new
"""
Name: DictComp
Flyable-version: v0.1a1
Description: Test the dict comprehension
"""
# Quail-test:start
vec = [1, 2, 3, 4]
{i: i + 2 for i in vec} # Quail-assert: eq {1: 3, 2: 4, 3: 5, 4: 6}
{i % 2: i for i in vec} # Quail-assert: eq {1: 3, 0: 4}
# Double each value in the dictionary
dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
{k:v*2 for (k,v) in dict.items()} # Quail-assert: eq {'a': 2, 'b': 4, 'c': 6, 'd': 8, 'e': 10}
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
{n:n**2 for n in numbers if n % 2 == 0} # Quail-assert: eq {0: 0, 8: 64, 2: 4, 4: 16, 6: 36}
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
# Quail-test:end


# Quail-test:new
"""
Name: Yield
Flyable-version: v0.1a1
Description: Test the yield expression
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: YieldFrom
Flyable-version: v0.1a1
Description: Test the YieldFrom expression
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: Compare
Flyable-version: v0.1a1
Description: Test the compare expression
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: Call
Flyable-version: v0.1a1
Description: Test the call expression (function call)
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: FormattedValue
Flyable-version: v0.1a1
Description: Test the FormattedValue expression (formats a value to a certain formatting)
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: JoinedStr
Flyable-version: v0.1a1
Description: Test the JoinedStr expression (Joining strings together)
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: Constant
Flyable-version: v0.1a1
Description: Test the constant expression (constant number, string, None, tuples, frozensets)
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: Attribute
Flyable-version: v0.1a1
Description: Test the Attribute expression (access to a value with the following ctx options: Load, Store or Del)
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: Subscript
Flyable-version: v0.1a1
Description: Test the subscript expression (subscripts an object, for example slicing of lists and tuples)
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: Starred
Flyable-version: v0.1a1
Description: Test the Starred expression (Access to a *var variable reference)
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: Name
Flyable-version: v0.1a1
Description: Test the name expression (variable name as a string with a the following ctx options: Load, Store, Del)
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: List
Flyable-version: v0.1a1
Description: Test the List expression
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: Tuple
Flyable-version: v0.1a1
Description: Test the tuple expression
"""
# Quail-test:start
# Quail-test:end


# Quail-test:new
"""
Name: Slice
Flyable-version: v0.1a1
Description: Test the slice expression (subscript of an object from a value to another)
"""
# Quail-test:start
# Quail-test:end