def solution(n):
    answer = 0
    fibo = [0] * (n + 1)
    fibo[0] = 0
    fibo[1] = 1

    for idx in range(2, n+1):
        fibo[idx] = fibo[idx-1] + fibo[idx-2]
    answer = fibo[-1] % 1234567
    return answer

print(solution(3))

print(solution(5))