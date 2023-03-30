def calc(arr):
    sumV = 0
    for i in arr:
        for j in arr:
            sumV += S[i][j]
    return sumV

def comb(k, M, start):
    global minV
    if k==M:
        B = list(set(T)-set(A))
        gap = abs(calc(A)-calc(B))
        if minV > gap:
            minV = gap
        return
    for i in range(start,N-M+k+1):
        A[k] = i
        comb(k+1,M,i+1)


TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    S = [list(map(int,input().split())) for _ in range(N)]
    M = N//2
    minV = 20000*16*16
    A = [-1] * M
    T = [i for i in range(N)]
    comb(0, M, 0)
    print(f'#{tc} {minV}')