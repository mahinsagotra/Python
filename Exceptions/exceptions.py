# Errors and Exceptions

# syntax error
# a = 5 print(a)  # raise a syntax error
# print(a))  # syntax error

# a = 5 + '10'    #typeError

# import somemodule  #import error

#a = 5
# b = c  # c not defined, name error

# file error
#f = open('somefile.txt')

# value Error
#a = [1,2,3]
# a.remove(4)    #valueError: x not in list
# print(a)

# Index Error
# a=[1,2,3]
# a[4]      #index out of range

# Key Error
#myDict = {'name': 'MAHIN'}
# myDict['age']          #age not present in my dictionary

# Raising an Exception, i.e, force an exception to occur in case of condition is met

#x = -5
# if(x < 0):
#    raise Exception('x should be positive')

#x = -10
#assert(x >= 0), 'x is not positive'

# Handle Exceptions


# x = 5/0     #zero division error

try:
    a = 5/0
except:
    print('an error happened')

# catch the type of exception
try:
    a = 5/0
except Exception as et:
    print(et)

try:
    a = 5/0
except ZeroDivisionError:
    print('excepted')

try:
    a = 5/0
    b = a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)

try:
    a = 5/1
    b = a + 4
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')

# finally clause runs always no matter if there's an ex eption or not
# it is used to make some cleanup operations
try:
    a = 5/1
    b = a + 4
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
# finally:
#    print('cleaning up....')

######
# How we can define our own Exceptions


class ValueTooHighError(Exception):
    pass


def test_value(x):
    if(x > 100):
        raise ValueTooHighError('Value is too High')


try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
