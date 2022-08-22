from random import randint
array=list(map(int,input().split()))
def Qsort(array, low, high):
    if (low < high):
        pivot=randint(low,high)
        i = low
        j = high
        while (i < j):     
            while array[i] <= array[pivot] and i < high:    
                i += 1
            while array[j] > array[pivot]:                  
                j -= 1
            if (i < j):
                array[i], array[j] = array[j], array[i]
        array[pivot], array[j] = array[j], array[pivot]
        Qsort(array, low, j - 1)
        Qsort(array, j + 1, high)
        return array
    else:
      return array
n = len(array)
print(Qsort(array, 0, n-1))


import random

array=[1,2,5]
sum = 11
while sum>0 :
    ran = random.choice(array)
    total = sum-ran
    if(total<0):
        continue
    sum=sum-ran
    print(ran)


