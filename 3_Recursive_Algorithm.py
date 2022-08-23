array = [1,2,5]
sum = 11
ans = []
def findmin(sum,array,ans):
    if sum==0:
        return ans
    a = (sum//max(array))
    for i in range(a):
        ans.append(max(array))
    sum-=a*max(array)
    array.remove(max(array))
    return findmin(sum,array,ans)
findmin(sum,array,ans)
print(ans)

