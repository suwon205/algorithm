T = int(input())

for tc in range(1,T+1):
    N = int(input())
    carrot = list(map(int, input().split()))
    carrot.sort()

    minV = 10000

    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if carrot[i] != carrot[i+1] and carrot[j] != carrot[j+1]:
                    A = i+1
                    B = j-i
                    C = N-1-j
                    if A*B*C != 0 and A<= N//2 and B <= N//2 and C <= N//2:
                        if minV > max(A,B,C)-min(A,B,C):
                            minV = max(A,B,C)-min(A,B,C)

    if minV == 10000:
        minV = -1
    print(f'#{tc} {minV}')