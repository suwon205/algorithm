def calc(i, st, plus, minus, multiply, divide):
    global minV
    global maxV

    if i == N:
        if minV > st:
            minV = st
        if maxV < st:
            maxV = st
        return

    if plus:
        calc(i + 1, st + lst[i], plus - 1, minus, multiply, divide)
    if minus:
        calc(i + 1, st - lst[i], plus, minus - 1, multiply, divide)
    if multiply:
        calc(i + 1, st * lst[i], plus, minus, multiply - 1, divide)
    if divide and st >= 0:
        calc(i + 1, st // lst[i], plus, minus, multiply, divide - 1)
    elif divide and st < 0:
        calc(i + 1, -((-st) // lst[i]), plus, minus, multiply, divide - 1)

N = int(input())
lst = list(map(int, input().split()))
operator = list(map(int, input().split()))

maxV = -1000000000
minV = 1000000000
calc(1, lst[0], *operator)
print(maxV)
print(minV)
