import math
def solution(num, idx, add, sub, mul, div):
    global maxV, minV
    if idx == N:
        maxV = max(maxV, num)
        minV = min(minV, num)
        return
    else:
        if add > 0:
            solution(num + nums[idx], idx + 1, add - 1, sub, mul, div)
        if sub > 0:
            solution(num - nums[idx], idx + 1, add, sub - 1, mul, div)
        if mul > 0:
            solution(num * nums[idx], idx + 1, add, sub, mul - 1, div)
        if div > 0:
            if num/nums[idx] < 0:
                solution(math.ceil(num / nums[idx]), idx + 1, add, sub, mul, div - 1)
            else:
                solution(num // nums[idx], idx + 1, add, sub, mul, div - 1)

T = int(input())
for tc in range(1, T + 1):
    maxV = -100000000
    minV = 100000000
    N = int(input())
    a, b, c, d = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    solution(nums[0], 1, a, b, c, d)
    print(f'#{tc} {maxV-minV}')