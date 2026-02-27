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

# ========================================================== Notes =====================================================================

"""

- The core problem that generators solve :
        Normal function -> Runs completely, Returns ONE value, Forgets everything after return
        Generator function -> Can Pause in the middle, Remembers its state, Resumes from where it left off, Can produce MULTIPLE values over time.



"""

# Example 1 :
# Normal function
def normal():
    return 1    # runs, returns, DIES

# Generator function
def generator():
    yield 1     # runs, PAUSES, remembers state, waits
    yield 2     # resumes here next time
    yield 3     # resumes here next time

gen = generator()

next(gen) # → 1   (paused after yield 1)
next(gen) # → 2   (paused after yield 2)
next(gen) # → 3   (paused after yield 3)
next(gen) # → StopIteration (nothing left)

# The function doesn't run when you call it -- it returns a generator object.
# It only runs when you call next() on it.

# =========================================================================================
# The Generator pipeline :

def read_logs(filepath):
    """Generator: yields one line at a time"""
    with open(filepath) as f:
        for line in f:
            yield line.strip()

def filter_errors(lines):
    """Generator: takes a generator, yields only error lines"""
    for line in lines:
        if "ERROR" in line:
            yield line          # Only pass through errors

def parse_log(line):
    """Generator: transforms each line into structured data"""
    parts = line.split(" - ")
    yield {"timestamp": parts[0], "message": parts[1]}


# Chain generators together — NOTHING runs until you iterate!
lines   = read_logs("server.log")      # Generator 1
errors  = filter_errors(lines)         # Generator 2 (wraps Generator 1)
parsed  = parse_log(errors)             # Generator 3 (wraps Generator 2)

for log in parsed:
    print(log)

# This is called a GENERATOR PIPELINE:

# File  →  read_logs  →  filter_errors  →  parse_log  →  your code
#          (yields        (yields only      (yields
#           lines)         errors)           dicts)

# Data flows one item at a time through the whole pipeline.
# Memory used: ~1 line at any point. File size doesn't matter.