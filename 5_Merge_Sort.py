array = list(map(int,input().split()))
def Msort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        Msort(left)
        Msort(right)
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i+=1
            else:
                array[k] = right[j]
                j+=1
            k+=1
        while i < len(left):
            array[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            array[k] = right[j]
            j+=1
            k+=1
Msort(array)
print(array)



