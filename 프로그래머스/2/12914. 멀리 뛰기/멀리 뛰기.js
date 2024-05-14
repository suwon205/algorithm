function solution(n) {
    if (n === 1) {
        return 1;
    } else if (n === 2) {
        return 2;
    }
    
    var dp = [];
    dp[0] = 0;
    dp[1] = 1;
    dp[2] = 2;
    
    for (i = 3; i <= n; i++) {
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567; // DP를 사용하여 경우의 수 계산
    }
    console.log(dp)
    return dp[n];
}