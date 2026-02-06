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

print("*" * 20, f"Dictionaries", "*" * 20)
#------------------------------- DICT -------------------------------------------

# Dictionaries -> are like object in JS

    # Empty dictionary
my_dict = {}

    # Dictionary with data
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

    # Different ways to create
scores = dict(math=95, english=87, science=92)

print(f"person : {person}")
print(f"scores : {scores}")

print("-" * 20, f"Accessing values", "-" * 20)

#Accessing values

    # Get values by key
print(person["name"])
print(person["city"])

    # Using get()
print(person.get("job"))
print(person.get("love", "IDK")) # this will return IDK because it's default value to be returned if love key is not found.

# Changing dictionaries

    # Add or update
person["email"] = "alice@email.com"  # Add new
person["age"] = 31                   # Update existing

print(f"update & add : {person}")

    # Remove items
del person["email"] # remove by key
print(f"del dict: {person}")

age = person.pop("age") # remove & return
print(f"pop dict: {age}") # -> this will return you the values that you've removed.

person.clear() # remove all items



# Dictionary methods
person = {"name": "Alice", "age": 30, "city": "New York"}

    # You can convert the keys into list to get access of per key.
per = list(person.keys())
print(per[1])

    # Get all keys, values, or items
print(person.keys())    # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Alice', 30, 'New York'])
print(person.items())   # dict_items([('name', 'Alice'), ...])

    # Check if key exists
if "name" in person:
    print("Name found!")

    # Update multiple values
person.update({"age": 31, "job": "Engineer"})
print(f"update: {person}")


# Nested dictionaries
    # Dictionary of dictionaries
students = {
    "alice": {"age": 20, "grade": "A"},
    "bob": {"age": 21, "grade": "B"},
    "charlie": {"age": 19, "grade": "A"}
}

print(f"Nested Dict keys : {students['alice'].keys()}")

    # Access nested data
print(students["alice"]["grade"])  # "A"
print(students["charlie"]["age"])  # 19


print("*" * 20, f"Tuples", "*" * 20)
#------------------------------- Tuples --------------------------------------

# Tuples are immutable => Tuples are like lists, but they can’t be changed once created. 
# Use tuples for data that shouldn't change

tea_types = ("Black_tea", "Green_tea", "Orange_tea")

    # Single item tuple needs comma!
single = (42,)  # Note the comma
not_tuple = (42)  # This is just 42 in parentheses

    # Without parentheses (implicit)
coordinates = 10, 20

# Accessing Items

    # Get items
print(f"Accessing the first item in TUPLE: {tea_types[0]}")
print(f"Accessing the last item in TUPLE: {tea_types[-1]}")

    # Slicing 
print(f"Slicing in TUPLE: {tea_types[0:2]}")

# Tuple unpacking

    #Unpack values
point = (3,5)
x,y = point

print(x,y) # this gives 3 & 5 [x = 3, y = 5]

    #Multiple assignment
a, b, c = 1, 2, 3
print(a,b,c)

    # Swap variables elegantly
x,y = y,x
print(x,y) # 5 & 3

# You can use type to check the type
print(type(point)) # <class 'tuple'>

print("*" * 20, f"Sets", "*" * 20)
#------------------------------- Sets --------------------------------------

# When you want to work with unique collections.
# Sets are collections that only store unique values. They automatically remove duplicates.

# Empty set (careful!)
empty_set = set()  # NOT {} - that's a dict!

# Set with values - both ways work
numbers = {1, 2, 3, 4, 5} # Just values not keys
fruits = set(["apple", "banana", "orange"])

# From a list (removes duplicates)
scores = [85, 90, 85, 92, 90]
unique_scores = set(scores)  # {85, 90, 92}
print(unique_scores)

    # Use set() for empty sets, not {}. Empty curly braces create a dictionary!

# Basic Operations

    #Add Items
colors = {"marron", "olive_green"}

colors.add("navy_blue")
print(colors)

    # Remove items
colors.remove("navy_blue")    # Error if not found
colors.discard("marron") # No error if not found
print(f"remove SET: {colors}")

    # Check membership
if "olive_green" in colors:
    print("You got most unqiue color")


# Common use cases

    # removes duplicate
names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
unique_names = list(set(names))
print(unique_names)  # ['Alice', 'Bob', 'Charlie']

    # Fast membership testing
allowed_users = {"alice", "bob", "charlie"}

if "alice" in allowed_users:  # Very fast!
    print("Access granted")

# ==============================================================
# Order is not guaranteed!
numbers = {3, 1, 4, 1, 5}
print(numbers)  # Could be any order

# Use list if order matters
ordered = [3, 1, 4, 1, 5]


"""

In programming, membership means checking whether a value exists inside a collection (like a list, set, or string).

It's commonly done with operators like in (Python) or methods like contains.

The result is usually true/false, depending on whether the value is found.


"""


