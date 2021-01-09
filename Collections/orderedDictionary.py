# Just like an ordinary Dictionary But they remember the order in which
# the values are inserted
from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['e'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

ordered_dict['a'] = 1
print(ordered_dict)

# After python 3.7 normal dictionary also remembers the order of the elements
ordered_dict1 = {}
ordered_dict1['e'] = 1
ordered_dict1['b'] = 2
ordered_dict1['c'] = 3
ordered_dict1['d'] = 4
print(ordered_dict1)

ordered_dict1['a'] = 1
print(ordered_dict1)
