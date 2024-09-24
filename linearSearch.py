def linear_search(arr, target):
    for index, values in enumerate(arr):
        if values == target:
            return index
    return index-1

numbers = [64, 34, 25, 12, 22, 11, 90]
print(linear_search(numbers, 22))