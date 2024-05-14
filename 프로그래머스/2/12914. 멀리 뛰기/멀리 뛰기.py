def solution(n):
    answer = 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    # 1칸이나 2칸을 뛸 수 있음
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    ans = dp[-1] % 1234567
    return ans