import sys

N = int(input())
ls = list(map(int, sys.stdin.readline().split()))

ans = []
cnt =1
maxV = 0
for i in range(N-1): #증가하는 수열 구하기
    if ls[i] <= ls[i+1]:
       cnt +=1
    else:
        if maxV<cnt:
            maxV = cnt
        cnt = 1
if maxV < cnt:
    maxV = cnt
cnt = 1
ls.append(99999)
for j in range(N-1): #감소하는 수열 구하기
    if ls[j] >= ls[j+1]:
        cnt += 1
    else:
        if maxV<cnt:
            maxV = cnt
        cnt = 1
if maxV<cnt:
    maxV = cnt
print(maxV)