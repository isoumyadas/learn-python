# Numbers

# python has two ways to store numbers:

# Integers - Whole numbers without decimals
age = 24
score = -10


# Floats - Numbers with decimal points
price = 12.45
temp = -5.5
pi = 3.14159

"""
    Whole numbers for counting things.
    Decimals for measurements and calculations.
"""

sum = 3 + 5
total = 78 - 45
multiply = 3 * 8
divide = 90 / 8
power = 4 ** 9
floorDivsion = 10 // 3   # This is called floor division (rounds down)


print("SUM:: ", sum)
print("TOTAL:: ", total)
print("MULTIPLY:: ", multiply)
print("DIVIDE:: ", divide)
print("POWER:: ", power)
print("Floor Divison:: ", floorDivsion)




# ============================== STRINGS ===================================

"""
- String is just fancy name for text.
"""

name = "soumya"
# You can give long string name in python using """fdsdfs""", after " = "
your_name = """YOuR NAME IS 
SOUMYA
"""

first_name = "soumya"
last_name = "das"

full_name = first_name + " " + last_name
long_dash = "-" * 30
print("fullname:: ", full_name)
print(long_dash)


# To check the length of a variable

print(len(full_name))

# ============================== Booleans ====================================
print(long_dash)
is_true = True
is_false = False

# conditional 

age = 18

can_vote = age >= 18
print(can_vote)
print(long_dash)
print(f"Hello, {full_name} you're {age} year's old")

is_18 = age == 18
is_not_18 = age != 17
is_greater_than_18 = age > 18
is_lower_than_18 = age < 18
is_greater_or_equal_than_18 = age >= 18
is_lower_or_equal_than_18 = age <= 18

print("is_18:: ", is_18)
print("is_not_18:: ", is_not_18)
print("is_greater_than_18:: ", is_greater_than_18)
print("is_lower_than_18:: ", is_lower_than_18)
print("is_greater_or_equal_than_18:: ", is_greater_or_equal_than_18)
print("is_lower_or_equal_than_18:: ", is_lower_or_equal_than_18)

#======================== Logical Operators ====================================

print(long_dash)

has_license = True;

# and operator

can_drive = age > 18 and has_license
print(can_drive)


# or operator
day = "Saturday"
is_weekend = day == "Saturday" or day == "Sunday"
print(is_weekend)

# not -> reverse the value

is_adult = age >= 18
is_child = not is_adult
print(is_child)


print(long_dash);

# shortcuts

    # Instead of doing 
value = 10;
value = value + 10

    # You can do;
value += 10
value *= 3

print(long_dash);

# =============================String methods==========================

text = "Python Programming"

print(text.upper())
print(text.lower())
print(text.title())

print(long_dash);

# =============================Finding & Replacing==========================

print("Programming" in text) # this returns boolean value
print(text.find("Python"))
print(text.find("Java")) # As this is not available it returns -1.

# How find works?
    # P  y  t  h  o  n     P  r  o  g  r  a  m  m  i  n  g
    # 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17

    # "Python" starts at the very first character
    # The first character in Python is at index 0
    # So .find("Python") returns 0
    # That’s why you get 0 as output.

    # If the substring is not found, .find() returns -1.

    # AND if you don't want that use index

# print(text.index("java")); # output -> ValueError: substring not found
print(text.index("Python"));

    # find() = safe search
    # index() = strict search


print(text.count("Python")) # output =>  1


# Replace
new_message = text.replace("Python", "Javascript")
print(new_message)
