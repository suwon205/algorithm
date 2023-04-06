def comb(k):
    if k == M:
        print(' '.join(map(str,res)))
    else:
        for i in range(N):
            res[k] = lst[i]
            comb(k+1)


N,M = map(int, input().split())
lst = [i+1 for i in range(N)]
res = [0] * M
comb(0)