def per(k, probability):
    global tmp
    if probability <= tmp: #작은 경우는 물론, 같은 경우도 백트래킹 해주어야 한다. 
        return
    if k==N:
        if probability > tmp:
            tmp = probability
    else:
        for i in range(N):
            if not used[i]:
                used[i] = True
                per(k+1, 0.01*arr[i][k]*probability)
                used[i] = False

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    tmp = 0.0
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [False] * N
    per(0,1)
    print(f'#{tc} {tmp*100:6f}')