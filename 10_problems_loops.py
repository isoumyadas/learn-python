# 1 : Given a list of numbers, count how many are positive

numbers = [1,-2,3,-4,5,6,-7,-8,9,10]

positive_nums = []

positive_nums_count = 0

for number in numbers:
    if number > 0:
        positive_nums_count += 1
        positive_nums.append(number)

print(f"Positive numbers are : {positive_nums}")
print(f"Positive numbers count is : {positive_nums_count}")


# You can do that same with list comphrension

positive_nums = [n for n in numbers if n > 0]


print("*" * 20)

# 2 : Calculate the sum of even numbers up to a given number n.

n = 10
sum_even = 0

for num in range(1, n+1):
    if num % 2 == 0:
        sum_even += num

print(sum_even)

print("*" * 20)

# 3 : Print the multiplication table for given number up to 10 , but skip the fifth iteration.

table_num = 2

for i in range(1,11):
    if i == 5: continue
    print(f"{table_num} x {i} = {table_num * i}")

print("*" * 20)

# 4 : Reverse a string using a loop.

normal_string = "hitesh sir"

reverse_string = ""

for i in normal_string:
    reverse_string = i + reverse_string

print(reverse_string)

print("*" * 20)

# 5 : Given a string, Find the First Non-Repeated Character.

repeated_string = "lionel_messi"


for char in repeated_string:
    print(char)
    if repeated_string.count(char) == 1:
        print("Char is", char)
        break

print("*" * 20)

# 6 : Compute the Factorial of a number using a while loop.

num_input = 5

factorial = 1

while num_input > 0:
    factorial *= num_input
    num_input -= 1

print(f"Factorial is {factorial}")

print("*" * 20)

# 7 : Keep asking the user for input until they enter a number between 1 to 10.

while True:
    user_input = int(input("Enter value between 1 to 10: "))
    if 1 <= user_input <= 10:
        print("Go it")
        break
    else:
        print("Enter valid number")

print("*" * 20)

#8 : Check a prime number

your_number = 29

is_prime = False

if your_number > 1:
    for i in range(2, your_number + 1):
        if (your_number % i) ==  0:
            is_prime = True
            break

print(is_prime)

print("*" * 20)

# 9 : Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate

items = ["sdfsdf", "banana", "orange", "apple", "mango", "apple"]

for item in items:
    if items.count(item) > 1:
        print(f"Found the duplicate: {item}")
        break

        # using set

unique_set = set()

for item in items:
    if item in unique_set:
        print(f"Found the duplicate: {item}")
        break
    unique_set.add(item)


# 10 : Implement an exponential backoff strategy that doubles the wait time between rides, starting from 1 second , but stops after 5 retries.
import time
attempts = 0
max_retries = 5
wait_time = 1

while attempts < max_retries:
    print("Attempt", attempts + 1, "- wait time", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1

       
