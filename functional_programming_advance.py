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

# =========================== Lambda expressions ==========================

"""
In python lambda expressions are one time anonymous functions that you don't need more than once.
"""

lambda_value = list(map(lambda item: item*4, my_list))
print(f"Lambda function result : {lambda_value}")

# List sorting

a = [(0,2), (4,3), (10,-1), (9,9)]

a.sort(key=lambda itme: itme[1])
print(f"Sorted Value with lambda is : {a}")

# ============================== List Comphrensions ==========================

first_list = [char for char in "hello"]
sec_list = [num for num in range(0,100)]
third_list = [num**2 for num in range(0,88)]
forth_list = [num**2 for num in range(0,100) if num % 2 == 0]

print(f"First list => {first_list}")
print(f"second list => {sec_list}")
print(f"third list => {third_list}")
print(f"forth list => {forth_list}")


# ============================ List comphrensions in dict & set ==================

#  In set => It's same as list just with {} 
first_list_set = {char for char in "hello"}
sec_list_set = {num for num in range(0,100)}
third_list_set = {num**2 for num in range(0,88)}
forth_list_set = {num**2 for num in range(0,100) if num % 2 == 0}

print(f"First list => {first_list_set}")
print(f"second list => {sec_list_set}")
print(f"third list => {third_list_set}")
print(f"forth list => {forth_list_set}")


# In dict

simple_list = {"a": 1, "b": 2}

my_dict = {k:v**2 for k,v in simple_list.items() if v % 2 == 0}
print(f"my_dict=> {my_dict}")

my_dict2 = {num:num*2 for num in [1,2,3]}
print(f"my_dict2=> {my_dict2}")


# 

some_list = ["a", "b", "c", "d", "a", "a", "c", "e", "f"]

duplicates = list({value for value in some_list if some_list.count(value) > 1})

print(f"Duplicates are : {duplicates}")