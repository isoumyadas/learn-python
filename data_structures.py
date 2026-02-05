# Lists -> are like array in JS

# Empty list
my_list = []

# List with items
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5, 3]
mixed = ["hello", 42, True, 3.14]  

# Accessing items

print(fruits[1]) # "banana" (second item)
print(fruits[0]) # "apple" (first item)

print(fruits[-1]) # "orange" (last item)
print(fruits[-2]) # "banana" (second last item)


print("-" * 20, f"Changing Lists", "-" * 20)

# Changing lists

    # Change an item
fruits[0] = "mango"
print(fruits) # ['mango', 'banana', 'orange']

    # Add items
fruits.append("grape") # Add to end
print(f"Append: {fruits}") # ['mango', 'banana', 'orange', 'grape']

fruits.insert(1, "kiwi") # Insert at position
print(f"Insert: {fruits}") # ['mango', 'kiwi', 'banana', 'orange', 'grape']

    # Remove items
fruits.remove("kiwi") # remove by value
print(f"remove: {fruits}") #['mango', 'banana', 'orange', 'grape']

fruits.pop()
print(f"pop: {fruits}") #['mango', 'banana', 'orange']

del fruits[2] # remove my index
print(f"del: {fruits}") #['mango', 'banana', 'orange']

print("-" * 20, f"List Methods", "-" * 20)

# List methods

    # Information
print(f"length: {len(numbers)}") # length
print(f"count: {numbers.count(3)}") # 2 (count occurrences)
print(f"index: {numbers.index(1)}") # 0 (find's the position)

    # Sorting
numbers.sort() # Sort in place
print(f"sorting: {numbers}") # [1, 2, 3, 3, 4, 5]

numbers.reverse() # reverse order
print(f"reverse: {numbers}") # [5, 4, 3, 3, 2, 1]

    # Copy
new_numbers = numbers.copy();
print(f"Copy: {new_numbers}")

print("-" * 20, f"Checking Lists", "-" * 20)

# Checking Lists

    # Check if item exists
if "mango" in fruits:
    print("Found Mango!")
else:
    print("Mango is unavailable")

    # Check if list is empty
if fruits:
    print("List has items")
else:
    print("List is empty")

    # Check the length then print
if len(fruits) > 2:
    print(fruits[2])
else:
    print("Their is no index greater than 2 or equal to 2")

    # Modifying while loop
nums = [1,2,3,4]

new_list = []
for num in nums:
    if num != 2:
        new_list.append(num)
nums = new_list

print(f"modifying: {nums}")

# Now this can be done by List comprehension
# numbers = [num for num in numbers if num != 2]
