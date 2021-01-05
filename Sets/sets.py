# Sets: unordered, mutable, no duplicates
myset = {1, 1, 2, 2, 3, 4}  #remove duplicates
print(myset)

#use set function
myset = set("Hello")    #Unordered
print(myset)

#create empty set
myset = {}  #its an empty dictionary
print(type(myset))

myset = set() #empty set
print(type(myset))

#Add Elements in Set
myset.add(1)
myset.add(2)
myset.add(3)

print(myset)
print(type(myset))

#remove elements with remove method
myset.remove(3)

print(myset)

#discard(): it also removes the elements but if the elements is not found
#this will not show any error

#clear() :it clears our set

#pop(): this will return an arbitrary value of our set and also removes it
print(myset.pop())

#Iterarte over our set

for i in myset:
    print(i)