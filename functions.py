# Defining function

def greet():
    print("Hola! soumya")


greet()

# Naming functions rules:
"""
1. Use lowercase letters (username)
2. Seprate words with underscore (get_username) (create_new_username)
3.  Be descriptive about what it does
"""

# function with logic

cities = {
    "MUMBAI": "30 DEGREE",
    "KOLKATA": "35 DEGREE",
    "DELHI": "45 DEGREE",
    "PUNE": "27 DEGREE"
}

def check_weather():
    temp = input("Enter the city: ")

    if temp != "": 
        temp = temp.upper()

    if temp in cities:
        result = cities[temp]
        print(f"Today the temperature in {temp} is {result}")
    else:
        print("City is unvailable")


check_weather()

# Functions with parameters

def greeting_with_name(name): 
    print(f"Hello, {name}!")


greeting_with_name("soumya")

def greet_fullname(firstname, lastname):
    print(f"Good morning, {firstname} {lastname}")

greet_fullname("soumyaranjan", "das")

# default values

def greet_dog_name(name="tommy"):
    print(f"Hello, {name}.....")

greet_dog_name()
greet_dog_name("Maniki")

    # Using keyword arguments
def greet_cat_name(name="billu"):
    print(f"Hello, {name}.....")

greet_cat_name(name="zaree")

# In functions their is local & global variable

tax = 90

def function_name():
    discount = 77
    t = tax + discount
    print(t)

function_name()
print("Global variable:: ", tax)
# print("Local variable:: ", discount) # you can't access local variable.

if True:
    no_idea = "soum"
    print("Okay")

print("Local variable in if coniditon:: ", no_idea) # you can take access of variable which is under the scope of if condition.

# Returning 

def calculate_area(width, height):
    area = width * height
    return area

room_area = calculate_area(10,12)
print(f"Room Size: {room_area} sq ft")

# returning multiple value from a  function

def simple_function():
    numbers = [1,2,3,4]
    first_number = numbers[0]
    last_number = numbers[-1]

    return first_number, last_number

f, l = simple_function()

print(f)
print(l)

# docstring

def soemthing(): 
    """
    Docstring for soemthing, able to understand what does this function do
    """
    pass

soemthing() # you'll get the info related to that function, while hoevering on the function call

# you can access with

print(soemthing.__doc__)
# help(soemthing())


# *args **kwargs

def super_func(*args, **kwargs):
    # args gives us tuple of values
    # kwargs gives us dict of key & Values
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func(1,2,3,45,5, num1=5, num2=33))

# Rule : params, *args, default_params (i="sam"), **kwargs

"""

=> You can learn about scope, global & local variables in `notes.md`

"""