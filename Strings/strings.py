# Strings: ordered, immutable, text representation
my_string = 'Hello World'
print(my_string)

my_string = 'I\'m a programmer'
print(my_string)
# OR
my_string = "I'm a programmer"
print(my_string)

# Triple Quotes: for multi line strings, used for documentation
my_string = """hello
World"""
print(my_string)

# no new line
my_string = """hello \
World"""
print(my_string)

my_string = "Hello Wolrd"
char = my_string[-11]
print(char)

# Cannot Change
#   my_string[0]='h'
print(my_string)

# slicing
my_string = "Hello World"
substring = my_string[1:5]
print(substring)
substring = my_string[::2]
print(substring)
substring = my_string[::-1]
print(substring)

# Concate 2 or more strings

greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)

# Iterate
for i in greeting:
    print(i, end="")
print()

# Check
if 'e' in greeting:
    print('yes')
else:
    print('no')

# can also check for substrings
if 'ell' in greeting:
    print('Yes')
else:
    print('No')

# More Useful Methods ---->
my_string = '      Hello World      '
print(my_string)

# to remove whitespace
print(my_string.strip())

# convert to Upper Case
my_string = 'Hello World'
print(my_string.upper())
print(my_string.lower())

print(my_string.startswith('He'))
print(my_string.startswith('World'))
print(my_string.endswith('orld'))


# find()
print(my_string.find('o'))
print(my_string.find('lo'))
print(my_string.find("oo"))

# count()
print(my_string.count('o'))

# replace
print(my_string.replace('World', 'Universe'))
print(my_string.replace('Worrrld', 'Universe'))  # can't find, so does nothing

# COnvert to List
my_string = 'How are you doing'
my_list = my_string.split()  # looks for each space and then splits it
print(my_list)

my_string = 'How,are,you,doing'
my_list = my_string.split(",")  # here we use the delimiter a comma
print(my_list)

# List to string
new_string = ''.join(my_list)
print(new_string)  # concatenate all the words

new_string = ' '.join(my_list)  # we put a space between the commas to
# include a space between our new string
print(new_string)

my_list = ['a'] * 6
print(my_list)

# bad
new_string = ''
for i in my_list:
    my_string += i
print(my_string)  # this is a bad code as string is immutable so this code
# will create a new string everytime, which is going to be a very costly operation

# we can do this

# good
my_string = ''.join(my_list)
print(my_string)

# Formatting Strings
# %, .format(), f-Strings

# %
var = "Tom"
my_string = " the variable is %s" % var
print(my_string)

var = 3
my_string = " the variable is %d" % var
print(my_string)

var = 3.67565656
my_string = " the variable is %f" % var  # by defualt 6 digits
my_string = " the variable is %.2f" % var  # 2digits
print(my_string)

# .format()

var2 = 6
my_string = " the variable is {}".format(var)
print(my_string)

my_string = " the variable is {:.2f} and {}".format(var, var2)
print(my_string)

# f-String !!!HIGHLY RECOMENDED
my_string = f"the variable is {var} and {var2}"
print(my_string)

my_string = f"the variable is {var*2} and {var2+11}"
print(my_string)
