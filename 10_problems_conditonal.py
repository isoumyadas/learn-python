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