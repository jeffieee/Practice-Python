def count_even_odd(numbers):
    odd_count= 0
    even_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(count_even_odd(numbers))
        