N = int(input())

idx = list(map(int, input().split()))
ans =[]

for i in range(N):
    ans.insert(i - idx[i], i+1)

print(*ans)