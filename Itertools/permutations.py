from itertools import permutations

a = [1, 2, 3]
perm = permutations(a)
print(list(perm))

perm = permutations(a, 2)  # length =2
print(list(perm))
