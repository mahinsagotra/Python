import numpy as np

# All 0s matrix
a = np.zeros(5)
print(a)

a = np.zeros((2, 3))
print(a)

# All 1s matrix
print(np.ones((4, 2, 2), dtype='int32'))

# Any other number
print(np.full((2, 2), 99))

# Any other number (full_like)
print(np.full_like(a, 4))
