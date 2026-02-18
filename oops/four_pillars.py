# 4 Pillars of OOP

"""
1. Encapsulation -> It is the binding of data and functions that manipulate that data.

2. Abstraction -> It means hiding of information or abstracting away information and giving access to only what's neccessary.

3. Inheritance -> It allows new objects to take on the properties of existing objects.

4. Polymorphism -> Poly means many & mor means so many forms.
"""

# 1. Encapsulation

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def callOutYourName(self):
        return f"hello, {self.name}"

player1 = PlayerCharacter('soumya', 23)
print(player1.name)


# 2. Abstraction
    # public and private
        # private : _name (_) infront of variable means its a private method or attribute, But their is no private variables. "_" means please dont touch this attribute or methods. (This shouldn't be modified)

class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name # This shouldn't be modified
        self._age = age # This shouldn't be modified
    
    def callOutYourName(self):
        return f"hello, {self._name}"

player1 = PlayerCharacter('soumya', 23)
print(player1._name)


# 3. Inheritance
class UserCharacter():
    def sign_in(self):
        print('Logged In')


class Wizard(UserCharacter):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power of {self.power}")


class Archer(UserCharacter):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"Attacking with arrows: arrows left - {self.num_arrows}")


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Nidhi', 100)

# Here we can have access of sign_in in both different class.
wizard1.sign_in()
archer1.sign_in()

# isistance is built in function in python.
print(isinstance(wizard1, Wizard)) # output will be : True
# If you do same with UserCharacter this will give True as it is subclass
# print(isinstance(wizard1, object)) # This will give True, as it wizard1 also inherits the object based class that comes with python.


# Polymorphism
# Calling the same method for different object.

def player_attack(char):
    char.attack()

player_attack(wizard1)
player_attack(archer1)

# for loop

for char in [wizard1, archer1]:
    char.attack()

# =============================== Super =====================================

class User(object):
    def __init__(self, email):
        self.email = email
    
    def sign_in(self):
        print(f"Logged IN")

class Wizard(User):
    def __init__(self,name, power, email):
        # Either you can use this 
        # User.__init__(self, email)
        # or this
        super().__init__(email)
        self.name = name
        self.power = power
    
    def attack(self):
        print(f"Attacking with power - {self.power}")

wiz1 = Wizard("Jaasu", 60, "jaadu@text.com")
print(wiz1.email)

# ==== Introspection ======

print(dir(wiz1)) # This will give all the methods and attributes that the wiz1 instance has.

