# Everything in python is object.
    # Because everything in python is built with class keyword.

"""
    What is object?
    -> Objects have methods like these and attributes that you can access    with the DOT method.

    So, with Oop we can create our own types, our own data types with different attributes and methods.

    OOP help us to write code that is repeatable, well organized and memory efficient.
"""

# Creating new class

class BigObject:
    pass

"""
__init__ after self whatever param is their we have pass the arguments for that.

Attributes are pieces of data that are dynamic
    -> When we instantiate an object, they are going to be unique to that specific object like name, age down below.

"""

class PlayerCharacter:
    # class object attribute (is not dynamic it is static) and every new object created with this class will have membership as default and it will be static.
    membership = True
    def __init__(self, name="BOB", age=20):
        if(PlayerCharacter.membership):
            self.name = name
            self.age = age
    
    def run(self):
        print("run")
    
    @classmethod
    def addthing_things(cls, num1, num2):
        #  we can instantiate the class
        # return cls('Teddy', num1 + num2)
        return num1 + num2
    
    @staticmethod
    def addthing_things2(num1, num2):
        return num1 + num2

player1 = PlayerCharacter("Tom", 23)
print("Player one:", player1.name)

# ============================ Excerise ===================================

#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age



# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("Condy", 2)
cat2 = Cat("Tom", 1)
cat3 = Cat("Bitter", 3)



# 2 Create a function that finds the oldest cat
def findsOldestCat(*args):
        older = max(args)
        return older


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"Oldest Cat is {findsOldestCat(cat1.age, cat2.age,cat3.age)} years old")

# ============================== @classmethod ===============================

# In class you can access the method without instantiate the class. 
# @classmethod is not used most often.
print(PlayerCharacter.addthing_things(2,3))

# when you used instantiate the class inside @classmethod
# player3 = PlayerCharacter.addthing_things(2,3)
# print(player3)



