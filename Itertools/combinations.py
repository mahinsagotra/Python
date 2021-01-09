from itertools import combinations, combinations_with_replacement

a = [1, 2, 3]
comb = combinations(a, 2)  # length mandatory
print(list(comb))

comb = combinations_with_replacement(a, 2)
print(list(comb))
