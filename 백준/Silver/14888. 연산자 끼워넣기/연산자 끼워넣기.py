N = int(input())
ls = list(map(int,input().split()))
pl, mi, mul, div = map(int, input().split())
maxV = -99999999999999999
minV = 9999999999999999


def solution(num, idx, add, sub, mul, div):
    global maxV, minV
    if idx == N:
        maxV = max(maxV, num)
        minV = min(minV, num)
        return

    if add > 0:
        solution(num + ls[idx], idx + 1, add - 1, sub, mul, div)
    if sub > 0:
        solution(num - ls[idx], idx + 1, add, sub - 1, mul, div)
    if mul > 0:
        solution(num * ls[idx], idx + 1, add, sub, mul - 1, div)
    if div > 0:
        solution(int(num / ls[idx]), idx + 1, add, sub, mul, div - 1)


solution(ls[0], 1, pl, mi, mul, div)
print(maxV)
print(minV)