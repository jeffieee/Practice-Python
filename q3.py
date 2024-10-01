# Question:
# Write a Python program that:

# Asks the user to input 5 numbers, one by one.
# Stores these numbers in a list.
# Prints the following:
# The list of numbers.
# The sum of all the numbers in the list.
# The largest and smallest number in the list.
# The list in reverse order.

n = 5
arr_list = []
# insert the inputed number one by one in the list
for i in range(n):
    num = int(input("Input a number: "))
    arr_list.append(num)
# sum of the list
def sum_list (arr):
    return sum(arr)
# largest item in the list
def largest_item (arr):
    return max(arr)
# smallest item in the list
def smallest_item (arr):
    return min(arr)
# reverse the list
def reverse_order (arr):
    return arr[::-1]
    
# display the answers
print(arr_list)
print(sum_list(arr_list))
print(largest_item(arr_list))
print(smallest_item(arr_list))
print(reverse_order(arr_list))
