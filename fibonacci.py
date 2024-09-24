def fibonacci(number):
    array =[0,1]
    
    while len(array) < number +1:
        nextFib = array[-1] + array[-2]
        array.append(nextFib)
    return array[:number +1]
            
number = 7

print(fibonacci(number))   