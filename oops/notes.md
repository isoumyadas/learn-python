## Intro
-> OOP is a way to organize code that uses objects and classes to represent real-world entities and behaviour.
-> In OOP, object has attributes thing that has specific data and can perform certain actions using methods.

`
1. Organizes code into classes and objects
2. Supports encapsulation to group data and methods together.
3. Enables inheritance for reusability and hierarchy.
4. Allows polymorphism for flexible method implementation.
5. Improves modularity, scalability and maintainability.
`
## Class

- A class is a collection of objects.
  - Classes are created by keyword class.
  - Attributes are the variables that belong to a class.
  - Attributes are always public and can be accessed using the dot(.) operator

```python

class Dog:
    species = "Canine"

    def __init__(self, name, age):
        self.name = name
        self.age = age

```

### __init__
- The __init__() method acts as a constructor in Python and is automatically executed when an object is created. 
- It is used to initialize the attributes of the object with the values provided at the time of object creation.

```python

class Dog:
    species = "Canine"

    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog("Citrine", 3)
print(dog1.name, dog2.name)

```
#### default parameters
```python

class Dog:
    species = "Canine"

    def __init__(self, name="BOB", age=1):
        self.name = name
        self.age = age

dog1 = Dog(3)
print(dog1.name, dog1.age)

```
#### Method with inheritance
-> When using inheritance, both parent and child classes can have __init__ methods.
```python
class A:
    def __init__(self):
        print("A init called")

class B(A):
    def __init__(self):
        super().__init__()   # Call parent __init__
        print("B init called")

obj = B()

```

### self
- Whenever we create an object from a class, self refers to the current object instance. 
- It is essential for accessing attributes and methods within the class.


<!-- 4 pillars -->

# Inheritance -> Allows a class (child class) to acquire properties and methods of another class (parent class).

- Promotes code reusability by sharing attributes and methods across classes.
- Simplifies maintenance through centralized updates in parent classes.
- Enables method overriding for customized subclass behavior.
- Supports scalable, extensible design using polymorphism.  

```python

class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)

class Dog(Animal):
    def sound(self):
        print(self.name, "barks")

d = Dog("Buddy")
d.info()      # Inherited method
d.sound()

```

### Super() Function
- super() function is used to call the parent class’s methods. 
- In particular, it is commonly used in the child class’s __init__() method to initialize inherited attributes. 
- This way, the child class can leverage the functionality of the parent class.

```python

# Parent Class: Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)

# Child Class: Dog
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # Call parent constructor
        self.breed = breed

    def details(self):
        print(self.name, "is a", self.breed)

d = Dog("Buddy", "Golden Retriever")
d.info()      # Parent method
d.details()   # Child method


```
### Types of Python Inheritance

1. Single Inheritance -> In single inheritance, a child class inherits from just one parent class.
```python

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  # Employee inherits from Person
    def show_role(self):
        print(self.name, "is an employee")

emp = Employee("Sarah")
print("Name:", emp.name)
emp.show_role()

```

2. Multiple Inheritance -> In multiple inheritance, a child class can inherit from more than one parent class.
```python

class Person:
    def __init__(self, name):
        self.name = name

class Job:
    def __init__(self, salary):
        self.salary = salary

class Employee(Person, Job): # Inherits from both Person and Job 
    def __init__(self, name, salary):
        Person.__init__(self, name)
        Job.__init__(self, salary)
    
    def details(self):
        print(self.name, "earns", self.salary)

emp = Employee("Shruti", 100000)
emp.details()

```

3. Multilevel Inheritance -> In multilevel inheritance, a class is derived from another derived class (like a chain).
   - Here Manager inherits from Employee and Employee inherits from Person. So Manager can use methods from both parent and grandparent.

```python

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  
    def show_role(self):
        print(self.name, "is an employee")

class Manager(Employee):  # Manager inherits from Employee
    def department(self, dept):
        print(self.name, "manages", dept, "department")

mgr = Manager("Joy")
mgr.show_role()
mgr.department("HR")

```

4. Hierarchical Inheritance -> In hierarchical inheritance, multiple child classes inherit from the same parent class.

```python

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  
    def role(self):
        print(self.name, "works as an employee")

class Intern(Person):  
    def role(self):
        print(self.name, "is an intern")

emp = Employee("David")
emp.role()

intern = Intern("Eva")
intern.role()

```
5. Hybrid Inheritance -> Hybrid inheritance is a combination of more than one type of inheritance.

```python

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  
    def role(self):
        print(self.name, "is an employee")

class Project:
    def __init__(self, project_name):
        self.project_name = project_name

class TeamLead(Employee, Project):  # Hybrid Inheritance
    def __init__(self, name, project_name):
        Employee.__init__(self, name)
        Project.__init__(self, project_name)

    def details(self):
        print(self.name, "leads project:", self.project_name)

lead = TeamLead("Sophia", "AI Development")
lead.role()
lead.details()

```


# Polymorphism

- Means "same operation, different behavior"
- It allows functions or methods with same name to work differently depending on the type of object they are working upon.
- Different types of Polymorphism
  - Compile-time polymorphism (using *args & **kwargs)
    - Method Overloading
  - Runtime Polymorphism
    - Method Overriding
    - Duck Typing
    - Operator Overloading

- Real Life Example: In a backend payment system, multiple payment options are available such as Credit Card, UPI, NetBanking and Wallet. All payment types use a common method named processPayment() but different implementations:

  - Credit Card Payment: validates card, talks to bank API
  - UPI Payment: redirects to UPI gateway
  - Wallet Payment: checks wallet balance
  - NetBanking Payment: redirects to bank login
  
- The method name remains the same, but the action changes based on the payment type.

## Types:

1. Compile-time 
   - Compile-time polymorphism means deciding which method or operation to run during compilation, usually through method or operator overloading.
   - Languages like C++ and Java support this
   - Python don't because it is dynamically typed it resolves method calls at runtime, not during compilation. So, true overloading isn't supported in Python
   - Similar behavior can be achieved using default or variable arguments.

- The multiply() method works with different numbers of inputs, mimicking compile-time polymorphism.
```python

class Calculator:
    def multiply(self, a=1, b=1, *args):
        result = a * b
        for num in args:
            result *= num
        return result

# Create object
calc = Calculator()

# Using default arguments
print(calc.multiply())            
print(calc.multiply(4))           

# Using multiple arguments
print(calc.multiply(2, 3))       
print(calc.multiply(2, 3, 4))

```

2. Runtime Polymorphism (Overriding)
  - This means that the behavior of a method is decided while program is running, based on the object calling it.
  - This happens through Method Overriding a child class provides its own version of a method already defined in the parent class. Since Python is dynamic, it supports this, allowing same method call to behave differently for different object types.

```python

class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Polymorphic behavior
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())

```

3. Polymorphism in Built-in Functions
   - Built in functions like len() & max() are polymorphic
   - They work with different data types and return results based on type of object passed.
```python

print(len("Hello"))  # String length
print(len([1, 2, 3]))  # List length

print(max(1, 3, 2))  # Maximum of integers
print(max("a", "z", "m"))  # Maximum in strings

```

4. In Functions
   
- Duck typing is a concept where an object’s suitability is determined by the methods and properties it has, not by its actual type.

- perform_task() does not check the type of the object.
- It only assumes the object has a use() method.
- Any object with a use() method will work.

```python

class Pen:
    def use(self):
        return "Writing"

class Eraser:
    def use(self):
        return "Erasing"

def perform_task(tool):
    print(tool.use())

perform_task(Pen())
perform_task(Eraser())

```

# Encapsulation

- Is the bundling of data (attributes) and methods (functions) within a class, restricting access to some components to control interactions. 
- A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.

```python

class Employee:
    def __init__(self, name, salary):
        self.name = name          # public attribute
        self.__salary = salary    # private attribute

emp = Employee("Fedrick", 50000)
print(emp.name)       
print(emp.__salary) # This cannot be accesed directly, because python does not store it as __salary internally, It automatically changes it to -> _Employee__salary
# You can access it using 
print(emp._Employee__salary)

```
### What does name mangaling mean?
- Name mangling is when Python automatically changes a double-underscore attribute (like __salary) to _ClassName__salary internally.
- It helps prevent accidental access or overriding in subclasses, but it does not make the attribute truly private.

## Why do we need Encapsulation?
1. Protects data from unauthorized access and accidental modification.
2. Controls data updates using getter/setter methods with validation.
3. Enhances modularity by hiding internal implementation details.
4. Simplifies maintenance through centralized data handling logic.
5. Reflects real-world scenarios like restricting direct access to a bank account balance.

## Access Specifiers
- Access specifiers define how class members (variables and methods) can be accessed from outside the class
- 3 Types:
  - Public
  - Protected
  - Private

1. Public Members
   - Public members are variables or methods that can be accessed from anywhere inside the class, outside the class or from other modules. 
   - By default, all members in Python are public. 
   - They are defined without any underscore prefix (e.g., self.name).
```python

class Employee:
    def __init__(self, name):
        self.name = name   # public attribute

    def display_name(self):   # public method
        print(self.name)

emp = Employee("John")
emp.display_name()   # Accessible
print(emp.name)      # Accessible

```

2. Protected Members
   - Protected members are variables or methods that are intended to be accessed only within the class and its subclasses. 
   - They are not strictly private but should be treated as internal. 
   - In Python, protected members are defined with a single underscore prefix (e.g., self._name).
```python

class Employee:
    def __init__(self, name, age):
        self.name = name       # public
        self._age = age        # protected

class SubEmployee(Employee):
    def show_age(self):
        print("Age:", self._age)   # Accessible in subclass

emp = SubEmployee("Ross", 30)
print(emp.name)        # Public accessible
emp.show_age()         # Protected accessed through subclass

```

3. Private Members
   - Private members are variables or methods that cannot be accessed directly from outside the class. 
   - They are used to restrict access and protect internal data. 
   - In Python, private members are defined with a double underscore prefix (e.g., self.__salary).
   - Python applies name mangling by internally renaming them (e.g., __salary becomes _ClassName__salary) to prevent direct access.
```python

class Employee:
    def __init__(self, name, salary):
        self.name = name          # public
        self.__salary = salary    # private

    def show_salary(self):
        print("Salary:", self.__salary)

emp = Employee("Robert", 60000)
print(emp.name)          # Public accessible
emp.show_salary()        # Accessing private correctly
# print(emp.__salary)    # Error: Not accessible directly

```
<!-- Methods -->

4. Declaring Protected and Private Methods
   - Use a single underscore (_) before a method name to indicate it is protected meant to be used within class or its subclasses.
   - Use a double underscore (__) to define a private method accessible only within class due to name mangling.

```python

class BankAccount:
    def __init__(self):
        self.balance = 1000

    def _show_balance(self):
        print(f"Balance: ₹{self.balance}")  # Protected method

    def __update_balance(self, amount):
        self.balance += amount             # Private method

    def deposit(self, amount):
        if amount > 0:
            self.__update_balance(amount)  # Accessing private method internally
            self._show_balance()           # Accessing protected method
        else:
            print("Invalid deposit amount!")
            
account = BankAccount()
account._show_balance()      # Works, but should be treated as internal
# account.__update_balance(500)  # Error: private method
account.deposit(500)         # Uses both methods internally

```

5. Getter and Setter Methods
   - Getter and setter methods are used to access and modify private attributes safely. Instead of accessing private data directly, these methods provide controlled access, allowing you to:
    - Read data using a getter method.
    - Update data using a setter method with optional validation or restrictions.

```python

class Employee:
    def __init__(self):
        self.__salary = 50000  # Private attribute

    def get_salary(self):    # Getter method
        return self.__salary

    def set_salary(self, amount):   # Setter method
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary amount!")

emp = Employee()
print(emp.get_salary())  # Access salary using getter

emp.set_salary(60000)   # Update salary using setter
print(emp.get_salary())

```

# Abstraction
- Data abstraction means showing only the essential features and hiding the complex internal details. 
- Technically, in Python abstraction is used to hide the implementation details from the user and expose only necessary parts, making the code simpler and easier to interact with.

1. Abstract Base Class
   - An Abstract Base Class (ABC) is used to achieve data abstraction by defining a common interface for its subclasses. 
   - It cannot be instantiated directly and serves as a blueprint for other classes.
   - Abstract classes are created using abc module and @abstractmethod decorator.
```python

from abc import ABC, abstractmethod

class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass  # Abstract method

class English(Greet):
    def say_hello(self):
        return "Hello!"

g = English()
print(g.say_hello())

```

2. Abstract Methods
   - Abstract methods are method declarations without a body defined inside an abstract class. 
   - They act as placeholders that force subclasses to provide their own specific implementation, ensuring consistent structure across derived classes.
```python

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # Abstract method, no implementation here

```