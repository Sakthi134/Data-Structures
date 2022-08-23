array = ['a','b','c','d','e','f','g','h','i','j','k']
i=0
n=len(array)
count1=1
while (array.count('-')<n-1):
    if i==n:
        i=0
    if array[i]!='-':
        if count1%4==0 or count1%10==4:
            count1+=1
            array[i]='-'
        if array[i]!='-':
            count1+=1
    i+=1
for j in array:
    if j!='-':
        print(j)