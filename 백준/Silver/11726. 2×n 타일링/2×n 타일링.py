N = int(input())
dp = [1,2]
cnt = 3
if N>=3:
    while N!=cnt:
        tmp = dp[1]+dp[0]
        dp[0] = dp[1]
        dp[1] = tmp
        cnt += 1
    print((dp[0]+dp[1]) % 10007)
else:
    print(dp[N-1])