# similar to normal dictionary, it just sets a default value if the value
# of the key is not set
from collections import defaultdict
d = defaultdict(int)

d['a'] = 1
d['b'] = 2
print(d)
print(d['a'])
print(d['a'])
print(d['c'])  # c is not present so it will print a default value which is 0.

dd = defaultdict(list)
