def per(k):
    if k == M:
        for i in range(M):
            print(res[i], end=' ')
        print()
    else:
        for i in range(N):
            if not used[i]:
                res[k] = lst[i]
                used[i] = True
                per(k+1)
                used[i] = False

N,M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
res = [0]*M
used = [False] * N
per(0)