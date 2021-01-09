# Doubly ended queue, add and remove from both ends
from collections import deque

d = deque()

d.append(1)
d.append(2)

d.appendleft(3)
print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.clear()
print(d)

d.extend([4, 5, 6])
print(d)

d.extendleft([1, 2, 3])
print(d)

d.rotate(1)
print(d)

d.rotate(2)
print(d)

d.rotate(-1)
print(d)
