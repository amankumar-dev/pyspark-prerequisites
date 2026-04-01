# 1) What is a function?
def temp():
    print('Hello world')
    
# 2) What are *args and **kwargs?
# *args: *args collects extra positional arguments into a tuple.
def args(*args):
    print(args)
args(1,2,3,4)

# **kwargs: **kwargs collects extra keyword arguments into a dictionary.
def kwargs(**kwargs):
    print(kwargs)
kwargs(name='aman',age=12)

# 3) What are lambda functions?
# It is a single line anonymous function
print((lambda x: x+10) (5))

# 4) What is a decorator?
# This is the high order function which take function as an argument and modify it
def decorator(func):
    def temp():
        print('Outer')
        func()
        print('Inner')
    return temp

@decorator
def func():
    print('func')
func()

# 5)What is a generator?
# This is the function which use yield method which run at a time
def temp():
    yield 1
    yield 'b'
    yield '@'
gen=temp()
print(next(gen))
print(next(gen))
print(next(gen))

# 6) Difference between yield and return?
# Yield return a single value at a time whereas return return all the values at once
