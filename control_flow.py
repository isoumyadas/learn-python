# Decision-making is everywhere
    # ATM : IF password correct, THEN allow access
    # APPS : IF user clicks button, THEN perform action
    # Weather apps : IF temp < 0, THEN show snow icon


# IF statements

score = 95

if (score >= 90):
    print("A - EXE")
elif (score >= 80):
    print("B - GOOD")
elif (score >= 70):
    print("C - KEEP IT UP")
else: 
    print("F - NEED IMPROVEMENT")


# Multiple conditions

age = 15
has_license = True

if(age >= 18 and has_license):
    print("You can drive")
elif(age < 18):
    print("Driving is only applicable for 18 or older than 18")
else:
    print("You can't Drive or You don't have license")


# if weekend or holiday:
#     print("NO work today");

# if not raining:
#     print("You can go outside")


has_ticket = True

if has_ticket:
    if age >=18:
        print("Enjoy your movie")
    else:
        print("Needs supervision")
else:
    print("Please buy the ticket")


print("-" * 20)

# for loops

# range is built-function. When you need for numbers
for i in range(5):
    print(i)


# looping over list
names = ["sam", "messi", "neymar"]

for name in names:
    print(f"Hey {name}")


# looping over string
for i in "Soumya":
    print(i)


# looping over dict
data = {"name": "soumya", "position": "Goalkeeper" }

for key in data:
    print(key)

#Looping over key & value

for key, value in data.items():
    print(f"{key} : {value}")


# When you should use range
for _ in range(5):
    print("Hello")


# Need index + value

x = ["Alice", "Bob", "Charlie"]

for i in range(len(x)):
    print(i, x[i])

# How many types of loops are their:
"""
Python has 2 core loop statements:
1. for
2. while

Everything else is built on top of for (not separate loop types like JS).

for loop used for:
    lists
    strings
    tuples
    sets
    dictionaries
    ranges
    generators

while loop (condition based)

while condition:
    do_something()

    use when:
        you don’t know how many times the loop will run
        loop depends on a condition

You can use => break, continue, pass 

    for x in data:
        if x == 5:
            break
    else:
        print("5 not found")


"""

