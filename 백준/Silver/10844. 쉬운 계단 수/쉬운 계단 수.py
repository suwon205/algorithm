N = int(input())
tmp = [0,1,1,1,1,1,1,1,1,1]
cnt = 0
while cnt != N-1:
    DP = tmp[:]
    tmp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for idx in range(10):
        if idx == 0:
            tmp[1] += DP[0]
        elif idx == 9:
            tmp[8] += DP[9]
        else:
            tmp[idx+1] += DP[idx]
            tmp[idx-1] += DP[idx]
    cnt += 1
if N == 1:
    print(sum(tmp))
else:
    print((sum(tmp))%1000000000)