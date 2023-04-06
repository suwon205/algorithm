def per(k):
    if k == M:
        if sorted(res) == res:
            for i in range(M):
                print(res[i], end=' ')
            print()
            return
    else:
        for i in range(N):
            if not used[i]:
                res[k] = lstn[i]
                used[i] = True
                per(k+1)
                used[i] = False

N,M = map(int, input().split())
lst = []
lstn = [n+1 for n in range(N)]
res = [-1] * M
used = [False] * N
per(0)