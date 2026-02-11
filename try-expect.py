# Basic try-expect structure

try:
    # Code that might cause an error
    risky_operation()
except:
    # Code that runs if there's an error
    print("Something went wrong")


# Catching specific errors

try:
    age = int(input("Enter your age: "))
    print(f"In 10 years, you'll be {age + 10}")
except ValueError:
    print("Please enter a number")


# Multiple error types

try:
    # Read a number from a file
    with open('number.txt', 'r') as f:
        text = f.read()
    number = int(text)
    result = 100 / number
    print(f"Result: {result}")
except FileNotFoundError:
    print("Could not find number.txt")
except ValueError:
    print("File doesn't contain a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")


#  Else clause => Code in else runs only if no error happened:

try:
    with open('data.txt', 'r') as f:
        data = f.read()
except FileNotFoundError:
    print("File not found")
else:
    # This only runs if the file was opened successfully
    print(f"File has {len(data)} characters")


# The finally clause
# Code in finally always runs, error or not:

try:
    file = open('data.txt', 'r')
    data = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    # This always runs to clean up
    if 'file' in locals() and not file.closed:
        file.close()
    print("Cleanup complete")


#  Raise critical errors

# Bad - hides all errors
try:
    critical_operation()
except Exception as e:
    print(f"Error: {e}")

# Good - log and re-raise
try:
    critical_operation()
except Exception as e:
    print(f"Critical error: {e}")
    raise  # Let the error propagate