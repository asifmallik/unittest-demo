import math

def sum(arr):
    num_sum = 0
    for x in arr:
        num_sum += x
    return x

def mean(arr):
    return sum(arr)/len(arr)

def variance(arr):
    arr_2 = []
    num_mean = mean(arr)
    
    for x in arr:
        arr_2.append((x - num_mean) ** 2)
    print(arr_2) 
    return mean(arr_2)

def standard_deviation(arr):
    return math.sqrt(variance(arr))
