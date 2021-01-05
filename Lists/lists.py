# Lists: ordered, mutable, allows duplicate elements
mylist = ['bananas', 'cherry', 'apple']
print(mylist)

mylist2 = list()
print(mylist2)

mylist3= [5, True, 'apple', 'apple']
item = mylist3[3]
print(item)
print(mylist3[-1]) #last element
print(mylist3[-3]) #third last element

for i in mylist3:
    print(i)

if 'bananas' in mylist:
    print('yes')
else:
    print('no')

#length of the list
print(len(mylist3))
print(len(mylist2))
print(len(mylist))

#appending elements
mylist2.append('lemon')
print(mylist2)

#insert at specific position
mylist3.insert(1, 'blueberry')
print(mylist3)

#remove items
#pop returns the last item and also removes it
mylist3.pop()
print(mylist3)

#remove a specific element
#mylist3.remove('cherry')
print(mylist3)

#remove all elements
mylist2.clear()
print(mylist2)

#reverse the list
print(mylist)
mylist.reverse()
print(mylist)

#sort the list
print(mylist)
mylist.sort()
print(mylist)

#sort() sorts the list inplace so it changes the original list 
mylist4 = [4, 3, 1, -1, -5, 10]
print(mylist4)
#mylist4.sort()
#print(mylist4)

#If we don't want to change the original list rather create a new list
#use sorted()
new_list = sorted(mylist4)
print(mylist4)
print(new_list)

#If we want to create a new list with the same elements multiple times
mylist5 = [0] * 5
print(mylist5)

#concate two list with '+' operator
m_list = mylist4 + mylist5
print(m_list)

#slicing: a way to access subparts of the list 
list = [1,2,3,4,5,6,7,8,9]

a=list[1:5]
print(a)
print(list[:5]) #no start index
print(list[1:]) #to the end of the list
print(list[::2]) #step index step =2
print(list[::-1]) # reverse list

#coping list
list_org = ['bananas','cherry', 'apple']
list_cpy = list_org

print(list_cpy)
print(list_org)
list_cpy.append('lemon')
print(list_cpy) #both the list refers to the same list inside the memory
print(list_org)

#actual copy the list using copy() where original list remains same

list_cpy = list_org.copy()
list_cpy.append('chips')
print(list_cpy)
print(list_org)

list_cpy =list_org[:] #slicing makes copy from start to end

#
#
#Important
#List Comprehension
#Elegant and fast way to create a new list from exiting list
a =[1,2,3,4,5,6]

b =[i*i for i in a] #Syntax: [expression then for-in-loop]

print(a)
print(b)