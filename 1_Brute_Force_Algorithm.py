from itertools import combinations_with_replacement
sum1 = 11
array = [1,2,5]
comb = []
for i in range(1,sum1+1):
    comb.append(combinations_with_replacement(array,i))
temp = []
for i in comb:
    for j in i:
        print(j)
        if sum(j)==sum1:
            temp.append(j)
print(*temp[0])