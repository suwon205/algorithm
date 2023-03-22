N = int(input())

lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))
DP = [0 for _ in range(N+1)]

for i in range(N): #시작일
    for k in range(i+lst[i][0],N+1): #시작일 다음 상담일
        if DP[k] < DP[i] + lst[i][1]: 
            DP[k] = DP[i] + lst[i][1]
print(DP[-1])