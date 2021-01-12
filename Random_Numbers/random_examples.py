import numpy as np
import secrets
import random as rd

a = rd.random()
print(a)

a = rd.uniform(1, 10)
print(a)

a = rd.randint(1, 10)
print(a)

a = rd.randrange(1, 10)
print(a)

a = rd.normalvariate(0, 1)
print(a)

mylist = list("ABCDEFGH")
a = rd.choice(mylist)
print(a)

a = rd.sample(mylist, 3)
print(a)

a = rd.choices(mylist, k=3)
print(a)

rd.shuffle(mylist)
print(mylist)


rd.seed(1)

print(rd.random())
print(rd.randint(1, 10))

rd.seed(2)

print(rd.random())
print(rd.randint(1, 10))

rd.seed(1)

print(rd.random())
print(rd.randint(1, 10))


rd.seed(2)

print(rd.random())
print(rd.randint(1, 10))

#########
a = secrets.randbelow(10)
print(a)

a = secrets.randbits(4)
print(a)

mylist = list('ABCDEFGH')
a = secrets.choice(mylist)
print(a)

#######

a = np.random.rand(3)
print(a)

a = np.random.rand(3, 3)
print(a)

a = np.random.randint(0, 10, 3)
print(a)

a = np.random.randint(0, 10, (3, 4))
print(a)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
np.random.shuffle(arr)
print(arr)

np.random.seed(1)
print(np.random.rand(3, 3))

np.random.seed(1)
print(np.random.rand(3, 3))
