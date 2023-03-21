N = int(input())
lst = []
for _ in range(N):
    T,P = map(int,input().split())
    lst.append((T,P))
dp = [0 for i in range(N+1)]
for i in range(N):
    for k in range(i+lst[i][0],N+1):
        if dp[k] < dp[i] + lst[i][1]:
            dp[k] = dp[i] + lst[i][1]

print(dp[-1])