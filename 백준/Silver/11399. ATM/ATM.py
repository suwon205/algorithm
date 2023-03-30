N = int(input())
lst = list(map(int, input().split()))
lst.sort()
ans = 0
for i in range(N):
    ans += sum(lst[:i+1])
print(ans)