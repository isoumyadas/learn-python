# What does generators mean?

"""
In Python, a generator is a special type of iterator that produces values one at a time using the yield keyword, instead of returning all values at once.44

Everything which is generator is iterable, but not everything whcih is iterable is generator.

EG: range() is a generator and it is iterable
    list() is a iterable but not a generator

Generators are really really useful when calculating large sets of data, particularly using long loops where we don't really want to store that memory and we don't need to calculate everything.


"""

# ========================================================================

# yield pauses the function, and runs function again when next() is called

def generator_func(num): 
    for i in range(num):
        yield i * 2

g = generator_func(100)
next(g) # 0
next(g) # 2
print(next(g)) # 4


# Steps to create generator func

def gen_fuc(num):
    for i in range(num):
        yield i

for item in gen_fuc(50):
    print(item)

print("*" * 20)

# Fibnacci number

def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fib(21):
    print(x)