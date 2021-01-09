"""
Lambda functions
A lambda function is a small (one line) anonymous function that is 
defined without a name. A lambda function can take any number of 
arguments, but can only have one expression. While normal functions 
are defined using the def keyword, in Python anonymous functions are 
defined using the lambda keyword.

lambda arguments: expression

Lambda functions are used when a simple function is used only once or 
for a short period in your code. It's most common use is as an argument 
to higher-order functions (functions that takes in other functions as 
arguments). They are also used along with built-in functions like map(), 
filter(), reduce().
"""
from functools import reduce


def add10(x): return x+10


x = print(add10(5))

# multiple arguments


def mult(x, y): return x*y


print(mult(2, 7))


"""
Usage example: Lamdba inside another function
Return a customized lambda function from another function and create 
different function variations depending on your needs.
"""

"""
Custom sorting using a lambda function as key parameter
"""
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D)

print(points2D)
print(points2D_sorted)

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key=lambda x: x[1])

print(points2D)
print(points2D_sorted)

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key=lambda x: abs(x[1]))

print(points2D)
print(points2D_sorted)

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key=lambda x: x[0]+x[1])

print(points2D)
print(points2D_sorted)

# map()
#map(func, seq)
a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print(list(b))

# list comprehension method
c = [x*2 for x in a]
print(c)

# filter()
# filter(func, seq)  must return true or false

a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)
print(list(b))

c = [x for x in a if x % 2 == 0]
print(c)

# reduce()
# reduce(func, seq)  repeadly applies the function to the elements and returns
# the single value
a = [1, 2, 3, 4, 5, 6]

prod_a = reduce(lambda x, y: x*y, a)
print(prod_a)
