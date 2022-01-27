"""
range
The range function allows you to quickly generate a list of integers,
this comes in handy a lot, so take note of how to use it!
There are 3 parameters you can pass, a start, a stop, and a step size. Let's see some examples:
"""
n = range(0, 11)
print(n)

n = list(range(0, 11))
print(n)

n = list(range(0, 11, 2))
print(n)

"""
enumerate
enumerate is a very useful function to use with for loops. Let's imagine the following situation:
"""

for i, letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i, letter))

"""
zip
Notice the format enumerate actually returns, let's take a look by transforming it to a list()
"""
mylist1 = [1, 2, 3, 4, 5]
mylist2 = ['a', 'b', 'c', 'd', 'e']
newlist = zip(mylist1, mylist2)
print(newlist)
newlist = list(zip(mylist1, mylist2))
print(newlist)

"""
random
Python comes with a built in random library. There are a lot of functions included in this random library, 
so we will only show you two useful functions for now.
"""
from random import shuffle
mylist = [10, 20, 30, 40, 100]
shuffle(mylist)
print(mylist)

from random import randint
x = randint(0, 100)
print(x)


