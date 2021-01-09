from itertools import count, cycle, repeat

for i in count(10):
    print(i)
    if i == 15:
        break

# cycle: this will cycle infinitely through an iterable
a = [1, 2, 3]
for i in cycle(a):
    print(i)
    if i == 3:
        break

# repeat: this will repeat infinitely
for i in repeat(1, 4):  # the second argument is the stop which will stop after 4 repetitions
    print(i)
