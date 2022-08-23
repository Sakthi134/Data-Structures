deno = list(map(int,input().split()))
def findCoin(V):
    n = len(deno)
    ans = []
    i = n - 1
    while(i >= 0):
        while (V >= deno[i]):
            V -= deno[i]
            ans.append(deno[i])
        i -= 1
    for i in range(len(ans)):
        print(ans[i], end = " ")
n = 11
print(end = " ")
findCoin(n)
      