N, M = map(int, input().split())
visited = [False] * (N+1)
res =[]
def partial(k):
    if k == M:
        print(' '.join(map(str, res)))
    for i in range(1,N+1):
        if not visited[i]:
            visited[i] = True
            res.append(i)
            partial(k+1)
            res.pop()
            visited[i] = False

partial(0)