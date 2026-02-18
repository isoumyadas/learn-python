"""

1. Dunder methods (short for “double underscore” methods) are special methods in Python that let you define how your objects behave with built-in operations.

eg:
__init__
__str__
__add__
__len__

-> They’re also called magic methods or special methods.

=> Dunder methods allow custom objects to integrate with Python’s built-in behavior and operators.

They allow your class to:

a. Work with operators (+, -, *)
b. Be printed nicely
c. Be compared (==, <)
d. Work with len()
e. Be iterable (for loop)
f. Support indexing (obj[0])
g. Behave like built-in types

=> Are automatically triggered by Python
=> Make custom classes behave like built-ins

"""

# Common Dunder Methods

# 1. __init__ -> Constructor
# This is called when an object is created


class Person:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.my_dict = {
            'name': "yoyo",
            'has_pets': False
        }
    
    def __str__(self):
        return f"Person: {self.name}"
    
    def __add__(self, other):
        if isinstance(other, Person):
            return self.value + other.value
        raise Exception("Invalid type")
    
    def __call__(self, *args, **kwds):
        return("yesss!")
    
    def __len__(self):
        return 6
    
    def __getitem__(self, i):
        return self.my_dict[i]
    
    
person1 = Person("Sam", 9)
person2 = Person("Gill", 8)

# 2. __str__ -> Human readable string
print(person1)

print(person1.__len__())
print(len(person1))
print(person1 + person2)

print(person1())
print(person1['name'])

# ====================== For Better Understanding ============================

class Book:

    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"`{self.name}` by {self.author}"
    
    def __eq__(self, other):
        return self.name == other.name or self.author == other.author
    
    def __repr__(self):
        return f"name={self.name}, author={self.author}, pages={self.pages}"
    
    def __lt__(self, other):
        return self.pages < other.pages
    
    def __gt__(self, other):
        return self.pages >  other.pages
    
    def __add__(self, other):
        if isinstance(other, Book):
            return f"{self.pages + other.pages} Pages"
        raise Exception("Invalid type")
    
    def __contains__(self, keyword):
        return keyword in self.name or keyword in self.author
    
    def __getitem__(self, key):
        if key == "name":
            return self.name
        elif key == "author":
            return self.author
        elif key == "pages":
            return self.pages
        else:
            return f"The key {key} was not found"

book1 = Book("Atomic Habits", "James Clear", 290)
book2 = Book("Stoic", "Ryan Holiday", 100)

# str
print(book1)

# eq
print(book1 == book2)

# repr
print(repr(book1))

# lower than
print(book1 < book2)

# greater than
print(book1 > book2)

# contains
print("Ryan" in book2)

# 
print(book1["name"])
print(book1["author"])
print(book1["pages"])
print(book1["audio"])

