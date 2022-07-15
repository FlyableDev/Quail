# Quail : A Unit Testing Utility for the Flyable Compiler

---

**But, what is a quail?** [That's a quail.](docs/ressources/quail.jpg)
So cute 🥺

## The idea behind Quail:

- The purpose of Quail is to be an easy to use, expandable and developper friendly framework to write unit tests for the
  Flyable compiler. It is built on top of pytest to have access to its vast set of tools and to integrate elegantly with
  IDEs

## What are Quail Tests?

Quail Tests are the meat and bones of the Quail unit testing utility.

## How do I setup Quail?

1. Open your terminal, and enter the command `python -m venv venv` to create a new python envrionment
2. In the same terminal enter the command `venv\Scripts\activate.bat` if you have a Windows
   and `venv/Scripts/activate` if you have a Mac or a Linux distro to enter the virtual environment
3. In the same terminal, enter the command `pip install --editable .`
4. If all went well, you should now be able to use the Quail cli from your terminal. Try entering the command `quail`
5. If it worked, enter the command `quail run` for the first time and it should have created a configuration file for you.
6. Change the configuration file depending on your machine and installation directories
7. Done! 🥳

## How to run my tests?

Running Quail tests is really simple. You can use the Quail CLI to do so.

#### Running unit tests:

Running all the unit tests: `quail run -u`

Running a specific test suite: `quail run -u <test_suite>`

#### Running integration tests

Running all the integration tests:
`quail run -i`

Running a specific integration test:
`quail run -i <test_name>`

## How do they work

They operate, in their most basic form, by:

1. Using the python interpreter to:
   1. Compile the lines of code in the test
   2. Running the test and saving the output of the `stdout` (standard out)
2. Using the flyable compiler to:
   1. Compile the lines of code in the test
   2. Running the test and saving the output of the `stdout` (standard out)
3. Comparing those outputs

## Anatomy of a Quail Test

First, let's look a typical Quail Test and analyse it:

```python
# Quail-test:new
"""
Name: basic_addition
Flyable-version: v0.1a1
Description: Test the addition operator on int
"""
# Quail-test:start
0 + 0  # Quail-assert: eq 0
0 + 1  # Quail-assert: eq 1
1 + 1  # Quail-assert: eq 2
-10 + 23  # Quail-assert: eq 13
# Quail-test:end
```

For now, let's ignore the weird comments starting with `# Quail-...` and focus on their content and overall structure.
Quail tests are separated in multiple sections:

1. The information section
2. The test body section

Let's look at them in further details

### The information section

This section is the first section of every Quail test and contains all the metadata related to the test.  
In our example, it's this part:

```python
"""
Name: basic_addition
Flyable-version: v0.1a1
Description: Test the addition operator on int
"""
```

As we can see, this section is placed in a python multiline string and contains the following:

- The `Name` tag followed by the name of the test (ex: `basic_addition`)
- The `Flyable-version` followed by the version of the Flyable compiler it's testing (ex: `v0.1a1`)
- A `Description` tag followed by the description of the what the Quail Test is, well... testing (
  ex: `Test the addition operator on int`)
- --Optional-- The `Timeout` tag followed by the amount of seconds to wait after compiling the test using flyable
- --Optional-- The `No-Wrap` tag followed by a boolean to indicate if Quail should by default wrap the test in a test_flyable function

### The body section

This section contains what really matters, _the lines of code to test_ !
In our example, it's this part:

```python
0 + 0  # Quail-assert: eq 0
0 + 1  # Quail-assert: eq 1
1 + 1  # Quail-assert: eq 2
-10 + 23  # Quail-assert: eq 13
```

It's the content of this section that will be compiled and ran by the python interpreter and the flyable compiler to see
if their outputs match at runtime. But how can we compare the stdout if there's no print calls? And, most of all, what's
up with those `# Quail-assert:...` anyway? Those are really good questions and I feel like it's time to address them!

### Quail tags

Let's come back to those weird comments that start with `# Quail-...`. They are called Quail tags and are part of what
makes Quail so flexible. Each Quail tag follow a specific syntax:  
`# Quail-<tag_type>:<tag_name> [value]`

Currently, they come in one of two types, **Quail-test** tags and **Quail-assert** tags.

#### Quail-test tags

`Quail-test` tags allow the Quail Parser to know how the test is divided and parse the correct sections at the correct
time. In our example, it's those:

```python
# Quail-test:new
# Quail-test:start
# Quail-test:end
```

To see every Quail-test tag and its effect, see [The list of Quail-test tags](docs/Quail-test_tags.md)

#### Quail-assert tags

`Quail-assert` tags tell the Quail Parser how to modify the current line to test something in particular. They also help
to remove boilerplate code and make the test more readable. In our example, it's those:

```python
# Quail-assert: eq 0
# Quail-assert: eq 1
# Quail-assert: eq 2
# Quail-assert: eq 13
```

To see every Quail-assert tag and its effect, see [The list of Quail-assert tags](docs/Quail-assert_tags.md)

## Where are Quail tests?

They are in _Flyable/tests/unit_tests_  
Quail tests are in the quailt*<x>.py files (quailt stands for quail test)  
In the same folder as this file must be a test*<x>.py file from which the tests will be ran

## How can I make my own?

Let's say I want to write a new test suite to test how _Flyable_ handles **lists** with Quail.  
First, we will see how to add a new quail test suite  
Second, we will see how to add a new quail test to a quail test suite

### Adding a New Quail Test Suite

1. For example, I'm going to make a new quail test suite nammed 'list' by typing `Quail new list`
2. I answer the prompts Quail shows me (you can also directly put your values in the command, see `Quail new --help`)
3. Done! 🥳

#### Adding a Test to an Existing Quail Test Suite

1. For example, I'm going to add a new test called 'creating_lists' by
   typing `Quail add list --test_name creating_lists`
2. I answer the prompts Quail shows me (you can also directly put your values in the command, see `Quail add --help`)
3. Done! 🥳
