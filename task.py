import math

array1 = [1, 2, 3]
array2 = [1, 2, 3]

def M(array): 
    M = 0
    for i in range(0, len(array)) :
        M = M + array[i]
    return M/len(array)


def task(array1, array2):
    sum1 = 0
    sum2 = 0
    for i in range(0, len(array1)) :
        sum1 = sum1 + (array1[i] - M(array1)) * (array2[i] - M(array2)) 
    for i in range(0, len(array1)) :
        sum2 = sum2 + ((array1[i] - M(array1)) ** 2) * ((array2[i] - M(array2)) ** 2)
    result = sum1 / math.sqrt(sum2)
    print(result)

task(array1, array2)

