N = int(input())
numbers = list(map(int, input().split()))
plus, minus, multiple, division = map(int, input().split())
minV = 99999999999999
maxV = -99999999999999
def calc(num, idx, p, m, mul, d):
    global minV, maxV
    if idx == N:
        maxV = max(maxV, num)
        minV = min(minV, num)
        return
    if p>0:
        calc(num + numbers[idx], idx+1, p-1, m, mul, d)
    if m>0:
        calc(num - numbers[idx], idx+1, p, m-1, mul, d)
    if mul>0:
        calc(num * numbers[idx], idx+1, p, m, mul-1, d)
    if d>0:
        calc(int(num / numbers[idx]), idx+1, p, m, mul, d-1)
calc(numbers[0],1,plus, minus, multiple, division)
print(maxV)
print(minV)