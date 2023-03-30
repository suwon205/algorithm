def par(k, curSum):
    global cnt
    if curSum > K:
        return
    if k == N: #부분집합 생성 완료
        if curSum == K:
            cnt += 1
    else:
        par(k+1, curSum+A[k])
        par(k+1, curSum)

T = int(input())
for tc in range(1,T+1):
    N,K = map(int, input().split())
    A = list(map(int, input().split()))
    result = [-1] * N
    tmp =[]
    cnt= 0
    par(0, 0)

    print(f'#{tc} {cnt}')