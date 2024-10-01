# Write a Python program that:

# Takes two integer inputs from the user.
# Stores these numbers in two separate variables.
# Performs the following operations:
# Adds the two numbers and stores the result in a variable called sum_result.
# Subtracts the second number from the first and stores the result in a variable called sub_result.
# Multiplies the two numbers and stores the result in a variable called mul_result.
# Print out all the results (sum_result, sub_result, and mul_result) with descriptive messages.

print("Input the first number: ")
first_int = int(input())
print("Input the second number: ")
second_int = int(input())

sum_result = first_int + second_int
sub_result = first_int - second_int
mul_result = first_int * second_int

print("The sum of two integer is " + str(sum_result))
print("The difference of two integer is " + str(sub_result))
print("The product of two integer is " + str(mul_result))