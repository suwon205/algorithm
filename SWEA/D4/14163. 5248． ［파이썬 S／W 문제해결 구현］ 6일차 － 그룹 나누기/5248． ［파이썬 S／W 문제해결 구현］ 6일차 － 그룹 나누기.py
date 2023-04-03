def dfs(s):
    stack = []
    stack.append(s)
    visited[s] = True
    while stack:
        v = stack.pop()
        for w in G[v]:
            if not visited[w]:
                visited[w] = True
                stack.append(w)

T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    lst = list(map(int, input().split()))
    visited = [False] * (N+1)
    #인접 리스트 만들기
    G = [[] for _ in range(N+1)]
    for idx in range(0, len(lst),2):
        v1 = lst[idx]
        v2 = lst[idx+1]
        G[v1].append(v2)
        G[v2].append(v1)
    cnt = 0
    for i in range(1,N+1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    print(f'#{tc} {cnt}')