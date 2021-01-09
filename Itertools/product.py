# itertools: product, permutations, combinations, accumulate, groupby,
# and iterators

from itertools import product

a = [1, 2]
b = [3, 4]
prod = product(a, b)  # cartesian product
print(list(prod))

prod = product(a, b, repeat=2)
print(list(prod))
