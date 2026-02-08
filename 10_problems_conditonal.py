# 1 : Classify a person's age group: Child(<13), Teenager (13-19), Adult (20-59), Senior(60+)

# user_age = input("Please give an age: ");
age = int(25) # change to user_age

if age < 13:
    print("You're a Child")
elif age < 20:
    print("You're a teenager")
elif age < 60:
    print("You're an adult")
else:
    print("You're senior citizen")


print("-" * 20)

#2 : Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

day = "wednesday"

price = 8 if age < 18 else 12

if day == "wednesday":
    price -= 2

print(f"Your movie ticket price is {price}")


print("-" * 20)

#3 : Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F(below 60)

student_score = 101

if student_score < 60:
    print("F")
elif student_score < 70:
    print("D")
elif student_score < 80:
    print("C")
elif student_score < 90:
    print("B")
elif student_score <= 100:
    print("A")
else:
    print("Score can't be more than 100")

print("-" * 20)

# 4 : Determine if a fruit is ripe, overripe or unripe based on its color (eg: Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe) 

fruit_ripeness_by_color = {"Green" : "Unripe", "Yellow" : "Ripe", "Brown" : "Overripe"}

fruit_name = "Apple"
color = "Yellow"

if fruit_name:
    ripeness = fruit_ripeness_by_color.get(color, "Unkown State")
    print(f"{fruit_name} is {ripeness}")
else:
    print("Please determine any fruit name")

    # Another way to do

fruit = "Apple"
fruit_color = "Brown"

if fruit == "Apple":
    if fruit_color == "Green":
        print(f"{fruit} is Unripe")
    elif fruit_color == "Yellow":
        print(f"{fruit} is Ripe")
    else:
        print(f"{fruit} is Overripe")
else:
    print("Please determine fruit name")

print("-" * 20)

# 5 : Suggest an activity based on the weather (eg: Sunny - Go for walk, Rainy - Read a book, Snowy - Build an snowman)

activity_based_on_weather = {"Sunny" : "Go for walk", "Rainy": "Read a book", "Snowy" : "Build on snowman"}

weather = "Rainy"

if weather:
    activity = activity_based_on_weather.get(weather, "NONE")
    print(f"It's {weather} - {activity}")
else:
    print("Please Determine Weather!")

print("-" * 20)

# 6 : Choose a mode of transportation based on the distance (eg: <3 km: Walk, 3-15 km: Bike, >15 km: Car)

distance = 2

if distance < 3:
    print("Walk")
    # transport = "Walk"
elif distance <=15:
    print("Bike")
else:
    print("Car")

# print(f"{transport}") # We can use transport variable inside the if else statement.

print("-" * 20)

# 7 : Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of expresso.

coffee_size = "Large"
is_extra_shot = True

# This looks messy:

if coffee_size == "Small":
    if is_extra_shot:
        print(f"Your order is small coffee with extra shot of expresso")
    else:
        print("Your order is one small coffee")
elif coffee_size == "Medium":
    if is_extra_shot:
        print(f"Your order is Medium coffee with extra shot of expresso")
    else:
        print("Your order is one Medium coffee")
elif coffee_size == "Large":
    if is_extra_shot:
        print(f"Your order is Large coffee with extra shot of expresso")
    else:
        print("Your order is one Large coffee")
else:
    print(f"Please determine correct Coffee size")

# Optimal way to do:

if is_extra_shot:
    coffee = f"{coffee_size} coffee with extra shot of expresso"
else: 
    coffee = f"{coffee_size} coffee"

print("Coffee:", coffee)


print("-" * 20)

# 8 : Check if a password is "Weak", "Medium", or "Strong". Criteria: <6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong)

password = "sdfsfadsfasdf"
password_len = len(password)

if password_len < 6:
    print("Password strength is weak")
elif password_len <= 10:
    print("Password strength is Medium")
else:
    print("Password is strong")


print("-" * 20)

# 9 : Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

year = 2026

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

print("-" * 20)

# 10 : Recommend a type of pet food based on the pet's species and age. (eg: DOG:  <2 years - Puppy food, Cat: >5years - Senior cat food).

pet_type = "Cat"
pet_age = 6

if pet_type == "Dog":
    if pet_age < 2:
        print("Puppy food")
    else:
        print("Dog Food")
elif pet_type == "Cat":
    if pet_age > 5:
        print("Senior Cat Food")
    else:
        print("Junior Cat Food")
else:
    print("Species not found")

    # Another way to do:
pet_food = {
    "Dog": {
        "young": "Puppy food",
        "adult": "Dog food"
    },
    "Cat": {
        "young": "Junior cat food",
        "senior": "Senior cat food"
    }
}

pet_type = "Dog"
pet_age = 6

if pet_type in pet_food:
    if pet_type == "Dog":
        print(pet_food["Dog"]["young"] if pet_age < 2 else pet_food["Dog"]["adult"])
    else:
        print(pet_food["Cat"]["senior"] if pet_age > 5 else pet_food["Cat"]["young"])
else:
    print("Species not found")
