# returns accumulated sums or any binary function given to it
from itertools import accumulate
import operator

a = [1, 2, 3, 4]
acc = accumulate(a)
print(list(acc))

acc = accumulate(a, func=operator.mul)
print(list(acc))

b = [2, 3, 5, 1, 4]
acc = accumulate(b, func=max)
print(list(acc))
