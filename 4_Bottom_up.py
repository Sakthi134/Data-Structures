array = [1,2,5]
array.sort(reverse=True)
amount = 11
arr = []
for i in range(1,amount+1):
    sum = i
    count=0
    j=0
    while sum>0:
        if sum>=array[j]:
            sum-=array[j]
            count+=1
        else:
            j+=1
    arr.append(count)
print(arr[-1])