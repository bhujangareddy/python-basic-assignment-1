# Task 1: Perform Basic Mathematical Operations

# Problem Statement: Write a Python program that does the following:
# 1.  Takes two numbers as input from the user.
# 2.  Performs the basic mathematical operations on these two numbers:
#       Addition
#       Subtraction
#       Multiplication
#       Division
# 3.  Displays the results of each operation on the screen.


#  Expected Output:
# The output should include the result of each operation performed, for example:
# Enter the first number: 5
# Enter the second number: 10

# Addition: 15
# Subtraction: -5
# Multiplication: 50
# Division: 0.5 

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# sum = num1 + num2
total = num1 + num2 # I changed the variable name from sum to total, because in python we have a built-in function named sum()
# We should not use the pre-defined keywords as variable names in our code
diff = num1 - num2
prod = num1 * num2
divison_quotient_val = num1 / num2

print() # This statement will add an extra line space in the output

print("Addition:", total) # No need extra space character at the end, because ',' charcater gives default separater value -> " "(Space caharcter)
print("Subtraction:", diff)
print("Multiplication:", prod)
print("Division:", divison_quotient_val)