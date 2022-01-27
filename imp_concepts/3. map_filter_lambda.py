"""
map function
The map function allows you to "map" a function to an iterable object.
That is to say you can quickly call the same function to every item in an iterable, such as a list. For example:
"""
def square(num):
    return num**2
my_nums = [1, 2, 3, 4, 5]
new_list = map(square, my_nums)
print(new_list)
new_list = list(map(square, my_nums))
print(new_list)

def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'even'
    else:
        return mystring[0]
mynames = ['John', 'Cindy', 'Sarah', 'Kelly', 'Mike']
new_list = list(map(splicer, mynames))
print(new_list)

"""
filter function
The filter function returns an iterator yielding those items of iterable for which function(item) is true. 
Meaning you need to filter by a function that returns either True or False. 
Then passing that into filter (along with your iterable) and you will get back only the results that would return True when passed to the function.
"""
def check_even(num):
    return num % 2 == 0
nums = [0,1,2,3,4,5,6,7,8,9,10]
new_nums = filter(check_even, nums)
print(new_nums)
new_nums = list(filter(check_even,nums))
print(new_nums)


"""
lambda expression
One of Pythons most useful (and for beginners, confusing) tools is the lambda expression. 
lambda expressions allow us to create "anonymous" functions. 
This basically means we can quickly make ad-hoc functions without needing to properly define a function using def.

Function objects returned by running lambda expressions work exactly the same as those created and assigned by defs. 
There is key difference that makes lambda useful in specialized roles:

lambda's body is a single expression, not a block of statements.
    The lambda's body is similar to what we would put in a def body's return statement. 
    We simply type the result as an expression instead of explicitly returning it. 
    Because it is limited to an expression, a lambda is less general that a def. 
    We can only squeeze design, to limit program nesting. lambda is designed for coding simple functions, and def handles the larger tasks.
"""
#Lets slowly break down a lambda expression by deconstructing a function:
# def square(num):
#     result = num**2
#     return result
#
# def square(num):
#     return num**2
#
# def square(num): return num**2
#
# lambda num: num ** 2

square = lambda num: num ** 2
print(square(4))
#Now Square function converted to lambda expression
#print(list(map(square, my_nums)))
print(list(map(lambda num: num ** 2, my_nums)))

new_add = lambda x, y: x + y
print(new_add(2, 6))


