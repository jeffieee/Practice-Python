# Question:
# Write a Python program that:

# Asks the user to input a number (n).
# Prints all the numbers from 1 to n using a for loop.
# Then, using a while loop, print all numbers from n down to 1.


def for_loop(num): 
    for i in range(1, num + 1):  
        print(i)

def while_loop(num):
    i = num  
    while i > 0:  
        print(i)
        i -= 1  
        
# Get user input and call the functions
n = int(input("Input a number: "))
for_loop(n)
while_loop(n)


