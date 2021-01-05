odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

#Union: combines elements of both sets without duplication
#will not modify the original sets they always will return new sets
u = odds.union(evens)
print(u)

odds.update(evens)
print(odds)

#Intersection: only take elements found in both the sets
# similarly intersection update()
i=evens.intersection(primes)
print(i)

evens.intersection_update(odds)
print(evens)

#Difference
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)
print(diff)

#difference update()
setA.difference_update(setB)
print(setA)

#Symmetric Difference: will return a set with all the elements from set A and
#set B but not in both

dif = setA.symmetric_difference(setB)
print(dif)

#symmetric_difference_update()
setA.symmetric_difference_update(setB)
print(setA)

#Subset
print(setA.issubset(setB))  #return boolean

print(setA.issuperset(setB))

#Coping 2 sets
setA={1,2,3,4,5,6}

setB=setA

setB.add(7)
print(setA)
print(setB)

#copy()
setC = setA.copy()
setD = set(setA)

#Frozen Set: also a collection data type, immutable version of normal set

a = frozenset([1,2,3,4,5,6,6])

print(a)

a.add(9)    #Error
print(a)

a.remove()  #Error

#But Union, Intersection and Difference will work

