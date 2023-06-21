N = int(input())
number = list(map(int, input().split()))
pl, mi, mul, div = map(int, input().split())
minV = 9999999999999
maxV = -9999999999999
def calc(tmp, idx, pl, mi, mul, div):
    global minV, maxV
    if idx == N:
        maxV = max(maxV, tmp)
        minV = min(minV, tmp)
    if pl>0:
        calc(tmp + number[idx], idx+1, pl-1, mi, mul, div)
    if mi>0:
        calc(tmp - number[idx], idx+1, pl, mi-1, mul, div)
    if mul>0:
        calc(tmp * number[idx], idx+1, pl, mi, mul-1, div)
    if div>0:
        calc(int(tmp / number[idx]), idx+1, pl, mi, mul, div-1)
calc(number[0],1,pl, mi, mul, div)
print(maxV)
print(minV)