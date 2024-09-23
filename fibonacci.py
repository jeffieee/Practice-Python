def fibonacci(number):
    array =[0]
    if(len(array) == 1):
        array.append(1)
    
    while len(array) <= number+1:
        for num in array:
            array.append(array[num] + array[num+1])
    
    return array
            
    
number = 7

print(fibonacci(number))   