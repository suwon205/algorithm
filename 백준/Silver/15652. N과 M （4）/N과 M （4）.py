def dfs(k):
    if len(res)==M:
        print(' '.join(map(str, res)))
        return
    else:
        for i in range(k,N+1):
            if not visit[i]:
                res.append(i)
                dfs(i)
                res.pop()


N,M = map(int, input().split())
res = []
visit = [False] * (N+1)

dfs(1)