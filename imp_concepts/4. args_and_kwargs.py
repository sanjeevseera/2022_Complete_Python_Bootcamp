"""
*args and **kwargs
Work with Python long enough, and eventually you will encounter *args and **kwargs.
These strange terms show up as parameters in function definitions. What do they do? Let's review a simple function:
"""

"""
*args¶
When a function parameter starts with an asterisk, 
it allows for an arbitrary number of arguments, and the function takes them in as a tuple of values. Rewriting the above function:
"""
def myfunc(*args):
    return sum(args)*.05
print(myfunc(40,60,20))
print(myfunc(40,6))

"""
**kwargs¶
Similarly, Python offers a way to handle arbitrary numbers of keyworded arguments. 
Instead of creating a tuple of values, **kwargs builds a dictionary of key/value pairs. For example:
"""


def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print(
            f"My favorite fruit is {kwargs['fruit']}")  # review String Formatting and f-strings if this syntax is unfamiliar
    else:
        print("I don't like fruit")

myfunc(fruit='pineapple')
myfunc()

"""
*args and **kwargs combined
You can pass *args and **kwargs into the same function, but *args have to appear before **kwargs
"""


def myfunc(*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"May I have some {kwargs['juice']} juice?")
    else:
        pass

myfunc('eggs', 'spam', fruit='cherries', juice='orange')
