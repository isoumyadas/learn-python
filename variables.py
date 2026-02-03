# naming rules allwoed:
    # user_name = "2"  
    # userName = "sam" 
    # age2 = 45   
    # _private = "secret"

# naming rules not allowed:
    # 2age = 44 (cannot start with number)                          
    # my-name = "Dave"  (no hypens [python thinks it's subtraction])        
    # my name = "Dave" (No spaces)                                      
    # class = "python"  (Can't use python keywords)

# This is called snake_case
user_age = 24
user_name = "sammy"
is_logged_in = True
shopping_cart_total = 49.99

# Avoid camelCase [You can use that, but avoid it]
# userName = "sam"


# Variables can change

score = 0

score = 30

score = 120

print("score:: ", score) # this will print 120


# Multi-line comments
"""
This is multi line comment

"""