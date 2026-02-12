# decorators have @ and name beside that.
# @classmethod
# @staticmethod

# What are decorators => A decorator in Python is a function that wraps another function (or class) to modify or extend its behavior without changing its actual code.

# example:

def my_decorator(func):
    def wrap_func():
        print("**********")
        func()
        print("**********")
    return wrap_func

@my_decorator
def hello():
    print("hello")

hello()

# Decorator Patterns
# *args means (any number of arguments you can pass it here)
# **kwargs means (key,value pairs of agruments you can pass it here)
# * You can learn more about this in functions.py

def your_decorator(func):
    def wrap_fuc(*args, **kwargs):
        func(*args, **kwargs)
    return wrap_fuc

@your_decorator
def just_msg(greeting,name, emoji=":}"):
    print(f"{greeting} {name} {emoji}")

just_msg("Hello", "Soumya", ":}}}}}")

# =======================================================================

# * Why do we need decorators?

# @authentication , @login, @logout

# =========================== Excersie ===================================

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

# Their will be a scenario where you have to run the function inside the authentication decorator if user is authenticated.
def authenticated(fn):
    def wrap_func(*args, **kwargs):
        if args[0]["valid"]:
            fn(*args, **kwargs)
        else:
            print("Invalid User")
    return wrap_func


@authenticated
def message_friends(user):
    if user["valid"] == True:
        print('message has been sent')
    else:
        print('message has not been sent')

message_friends(user1)