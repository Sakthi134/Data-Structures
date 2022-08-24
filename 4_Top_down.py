array = [1,2,5]
sum = 11
comb = []
while(sum>0):
    if(max(array)<=sum):
        comb.append(max(array))
        sum-=max(array)
    if(max(array)>sum):
        array.remove(max(array))
print(comb)