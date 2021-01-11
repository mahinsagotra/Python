Errors and Exceptions¶
A Python program terminates as soon as it encounters an error. In Python, an error can be a syntax error or an exception. In this article we will have a look at:

Syntax Error vs. Exception
How to raise Exceptions
How to handle Exceptions
Most common built-in Exceptions
How to define your own Exception
Syntax Errors
A Syntax Error occurs when the parser detects a syntactically incorrect statement. A syntax error can be for example a typo, missing brackets, no new line (see code below), or wrong identation (this will actually raise its own IndentationError, but its subclassed from a SyntaxError).

In [5]:
a = 5 print(a)
File "<ipython-input-5-fed4b61d14cd>", line 1
a = 5 print(a)
^
SyntaxError: invalid syntax
Exceptions
Even if a statement is syntactically correct, it may cause an error when it is executed. This is called an Exception Error. There are several different error classes, for example trying to add a number and a string will raise a TypeError.

In [6]:
a = 5 + '10'

---

TypeError Traceback (most recent call last)
<ipython-input-6-893398416ed7> in <module>
----> 1 a = 5 + '10'

TypeError: unsupported operand type(s) for +: 'int' and 'str'
Raising an Exception
If you want to force an exception to occur when a certain condition is met, you can use the raise keyword.

In [4]:
x = -5
if x < 0:
raise Exception('x should not be negative.')

---

Exception Traceback (most recent call last)
<ipython-input-4-2a9e7e673803> in <module>
1 x = -5
2 if x < 0:
----> 3 raise Exception('x should not be negative.')

Exception: x should not be negative.
You can also use the assert statement, which will throw an AssertionError if your assertion is not True. This way, you can actively test some conditions that have to be fulfilled instead of waiting for your program to unexpectedly crash midway. Assertion is also used in unit testing.

In [7]:
x = -5
assert (x >= 0), 'x is not positive.'

# --> Your code will be fine if x >= 0

---

AssertionError Traceback (most recent call last)
<ipython-input-7-f9b059c51e45> in <module>
1 x = -5
----> 2 assert (x >= 0), 'x is not positive.'
3 # --> Your code will be fine if x >= 0

AssertionError: x is not positive.
Handling Exceptions
You can use a try and except block to catch and handle exceptions. If you can catch an exceptions your program won't terminate, and can continue.

In [8]:

# This will catch all possible exceptions

try:
a = 5 / 0
except:
print('some error occured.')

# You can also catch the type of exception

try:
a = 5 / 0
except Exception as e:
print(e)

# It is good practice to specify the type of Exception you want to catch.

# Therefore, you have to know the possible errors

try:
a = 5 / 0
except ZeroDivisionError:
print('Only a ZeroDivisionError is handled here')

# You can run multiple statements in a try block, and catch different possible exceptions

try:
a = 5 / 1 # Note: No ZeroDivisionError here
b = a + '10'
except ZeroDivisionError as e:
print('A ZeroDivisionError occured:', e)
except TypeError as e:
print('A TypeError occured:', e)
some error occured.
division by zero
Only a ZeroDivisionError is handled here
A TypeError occured: unsupported operand type(s) for +: 'float' and 'str'
else clause
You can use an else statement that is run if no exception occured.

In [9]:
try:
a = 5 / 1
except ZeroDivisionError as e:
print('A ZeroDivisionError occured:', e)
else:
print('Everything is ok')
Everything is ok
finally clause
You can use a finally statement that always runs, no matter if there was an exception or not. This is for example used to make some cleanup operations.

In [10]:
try:
a = 5 / 1 # Note: No ZeroDivisionError here
b = a + '10'
except ZeroDivisionError as e:
print('A ZeroDivisionError occured:', e)
except TypeError as e:
print('A TypeError occured:', e)
else:
print('Everything is ok')
finally:
print('Cleaning up some stuff...')
A TypeError occured: unsupported operand type(s) for +: 'float' and 'str'
Cleaning up some stuff...
Common built-in Exceptions
You can find all built-in Exceptions here: https://docs.python.org/3/library/exceptions.html

ImportError: If a module cannot be imported
NameError: If you try to use a variable that was not defined
FileNotFoundError: If you try to open a file that does not exist or you specify the wrong path
ValueError: When an operation or function receives an argument that has the right type but an inappropriate value, e.g. try to remove a value from a list that does not exist
TypeError: Raised when an operation or function is applied to an object of inappropriate type.
IndexError: If you try to access an invalid index of a sequence, e.g a list or a tuple.
KeyError: If you try to access a non existing key of a dictionary.
In [ ]:

# ImportError

import nonexistingmodule

# NameError

a = someundefinedvariable

# FileNotFoundError

with open('nonexistingfile.txt') as f:
read_data = f.read()

# ValueError

a = [0, 1, 2]
a.remove(3)

# TypeError

a = 5 + "10"

# IndexError

a = [0, 1, 2]
value = a[5]

# KeyError

my_dict = {"name": "Max", "city": "Boston"}
age = my_dict["age"]
Define your own Exceptions
You can define your own exception class that should be derived from the built-in Exception class. Most exceptions are defined with names that end in 'Error', similar to the naming of the standard exceptions. Exception classes can be defined like any other class, but are usually kept simple, often only offering a number of attributes that allow information about the error to be extracted by handlers.

In [11]:

# minimal example for own exception class

class ValueTooHighError(Exception):
pass

# or add some more information for handlers

class ValueTooLowError(Exception):
def **init**(self, message, value):
self.message = message
self.value = value

def test_value(a):
if a > 1000:
raise ValueTooHighError('Value is too high.')
if a < 5:
raise ValueTooLowError('Value is too low.', a) # Note that the constructor takes 2 arguments here
return a

try:
test_value(1)
except ValueTooHighError as e:
print(e)
except ValueTooLowError as e:
print(e.message, 'The value is:', e.value)
Value is too low. The value is: 1
