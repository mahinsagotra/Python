# Collections:  Counter, namedtuple, OrderedDict, defaultDict, deque
from collections import Counter, namedtuple

a = 'aaaabbbbbccc'
my_counter = Counter(a)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())

print(my_counter)
print(my_counter.most_common(2))  # returns a list with tuples in it

print(my_counter.most_common(1)[0][0])

print(list(my_counter.elements()))

# namedtuple object type similar to a struct
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)
print(pt.x)
print(pt.y)
