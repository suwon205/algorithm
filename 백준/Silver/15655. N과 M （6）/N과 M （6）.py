def comb(k,s):
    if k == M:
        for i in range(M):
            print(res[i], end=' ')
        print()
    else:
        for i in range(s,N):
            res[k] = lst[i]
            comb(k+1,i+1)

N,M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
res = [0] * M
comb(0,0)