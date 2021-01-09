# returns keys and groups from an iterrable
from itertools import groupby


def smaller_than_three(x):
    return x < 3


a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_three)
# print(list(group_obj))

for key, value in group_obj:
    print(key, list(value))

# lambda are small oneline fucntions that can have one line fucntiion
# that can have an input and then do some expression and will return the
# output

b = [5, 2, 1, 4]
group_obj = groupby(b, key=lambda x: x < 3)

for key, value in group_obj:
    print(key, list(value))


persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27}, {'name': 'CLaire', 'age': 28}]

group_persons = groupby(persons, key=lambda x: x['age'])
for key, value in group_persons:
    print(key, list(value))
