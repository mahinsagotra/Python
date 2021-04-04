import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a)

print(a.shape)

# Get a specific element [r,c]
print(a[1][5])
print(a[1][-1])

# Get a specific row
print(a[0, :])

# Get a specific column
print(a[:, 2])

# Getting a little fancy [startindex:endindex:stepsize]
print(a[0, 1:6:2])
print(a[0, 1:-1:2])

# Change
a[1, 5] = 20
print(a[1, 5])
print(a)

a[:, 2] = 5
print(a)

a[:, 2] = [1,2]
print(a)

# 3-D
b= np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)

#Getting a specific element (work outside in)
print(b[0,1,1])
print(b[0,1,:])
print('///////')
print(b[:,1,:])

b[:,1,:] = [[9,9],[8,8]]
print(b)