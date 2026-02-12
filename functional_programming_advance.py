# scope & closure
# import apis

def chai_coder(num):
    def actual(x):
        return x * num
    return actual

f = chai_coder(2) # this params goes to num
g = chai_coder(3)

print(f(3)) # this params goes to x
print(g(3))

# ====================== Functional Programming =========================

print(f"in funci :: {__name__}")

"""
1. Clear + Understandable

2. Easy to Extend

3. Easy to Maintain

4. Memory Efficient

5. DRY
"""

# ======== MAP =============

my_list = [1,2,3]

def multiply_by_2(item):
    return item * 2

my_updatedlist = list(map(multiply_by_2, my_list)) # This creates new list (with updated values)
print(f"Updated list => {my_updatedlist}")
print(f"OG list => {my_list}")


# ========== Filter ===============

def filter_odd(item):
    return item % 2 != 0

filtered_list = list(filter(filter_odd, my_list)) # Fitlers the og list according to condition
print(f"Filtered List -> {filtered_list}")


# =============== ZIP ==================

your_list = [10,20,30]
their_list = (5,4,9)

zipped_list = list(zip(my_list, your_list, their_list))
print(f"zipped list: {zipped_list}")


# =============== REDUCE =================

from functools import reduce

def accumulator(acc, item):
    return acc + item

reducedValue = reduce(accumulator, my_list, 0)
print(f"Reduced value: {reducedValue}")

