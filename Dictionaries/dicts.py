# Dictionary: Key-Value pairs, Unordered, Mutable

mydict = {'name':'Mahin', 'age': 28, 'city': 'Jammu'}

print(mydict)

mydict2 = dict(name='Marry', age=27, city='Kashmir')
print(mydict2)

value = mydict['name']
print(value)

#value = mydict['lastname']
#print(value)


mydict['email'] = 'max@xyz.com'
print(mydict)

#delete
del mydict['email']
print(mydict)

#can also use pop()
mydict.pop('age')
print(mydict)

#aslo popitem() removes last inserted item
mydict2.popitem()
print(mydict2)

#check if a key is inside the dictionary

if 'name' in mydict:
    print(mydict['name'])

#OR
try:
    print(mydict['lastname'])
except:
    print('Error')

#loop through dict

for key in mydict:
    print(key)

#for key in mydict.keys():
#   print(key)

for value in mydict.values():
    print(value)

#BOTH 

for key, value in mydict.items():
    print(key, value)

#Copy A Dictionary
mydict_copy = mydict

print(mydict_copy)

#If we modify the copy, it will also modify the original one
mydict_copy['email']='max@xad.com'

print(mydict_copy)
print(mydict)

#So if we want to make a separate copy we can do this copy()
mydict_copy = mydict.copy()
mydict_copy['email']='max@xaaaad.com'

print(mydict_copy)
print(mydict)

#OR we can use the dict()
mydict_copy = dict(mydict)
mydict_copy['email']='max@xaaaad.com'

print(mydict_copy)
print(mydict)

#Merge two dictionaries

my_dict ={'name': 'Max', 'age':28, 'email': 'max@xyz.com'}
my_dict_2 = dict(name='Marry', age=27, city='Boston')

my_dict.update(my_dict_2)
print(my_dict)
print(my_dict_2)

#we can use any immutable elments.
#Numbers as a key or a tuple if it only contains immutable elements
#

my_dict={3:9, 6:36, 9:81}
print(my_dict)

#value = my_dict[0]  #raises an exception as key '0' is not present

#or
mytuple = (8,7)
mydict= {mytuple: 15}

print(mydict)

##LISTS are not Possible as keys as it is mutable and can be changed after
#its creation and therefore it also not hashabe so it cannot be used as a key.
