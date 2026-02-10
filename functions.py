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