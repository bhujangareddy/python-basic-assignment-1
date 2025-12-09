# Task 2: Create a Personalized Greeting

# Problem Statement: Write a Python program that:
# 1.  Takes a user's first name and last name as input.
# 2.  Concatenates the first name and last name into a full name.
# 3.  Prints a personalized greeting message using the full name.

# Expected Output:
# The program should output a greeting like:

# Enter your first name: John
# Enter your last name: Doe

# Hello, John Doe! Welcome to the Python program.

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# print() # this statement adds an extra line space in the o/p console

# full_name = first_name + " " + last_name + "!"
# print("Hello,", full_name, "Welcome to the Python program.")

# We can use either above or below approach, which gives the same o/p string in the console

full_name = first_name + " " + last_name

print("Hello,", full_name + "!", "Welcome to the Python program.")