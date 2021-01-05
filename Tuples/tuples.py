# Tuple: ordered, immutable, allows duplicate elements
#cannot be changed after its creation


mytuple = ("Max", 28, "Boston") #parenthesis are optional
#mytuple = "Max", 28, "Boston"
print(type(mytuple))

#tuple = ("Max") #not a tuple, recognized as a string
#So for a single element we use
#tuple = ('Max')
print(type(tuple))


#use tuple() function
thistuple = tuple(('apple','banana','cherry')) # don't know why its not working
print(thistuple)

#Count elements in tuples
my_tuple =('a','b','p','q','l','e')

print(my_tuple.count('a'))

#index of a particular element
print(my_tuple.index('p'))

# We can easily convert tuple to a list and vice versa
my_list = list(my_tuple)
print(my_list)

my_tuple2 = tuple((my_list))
print(my_tuple2)

#slicing with tuples to acces subparts of tuple
a=(1,2,3,4,5,6,7,8)

b=a[2:5]
print(b)
b=a[:5]
print(b)
b=a[2:]
print(b)

b=a[::2]
print(b)

b=a[::-1]   # to reverse tuple
print(b)

my_tuple = 'Max', 29, 'Boston'

name,age,city= my_tuple
print(name)
print(age)
print(city)

my_tuple = (0, 1, 2, 3, 4, 5)

i1, *i2, i3=my_tuple    #*i2 will get the data in between

print(i1)
print(i3)
print(i2)   #returns a list