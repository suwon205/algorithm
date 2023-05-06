from collections import deque

def bfs(compo):
    q = deque()
    q.append(compo)
    visited[compo] = True
    while q:
        tmp = q.popleft()
        for k in graph[tmp]:
            if not visited[k]:
                visited[k] = True
                q.append(k)
    return

N,M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    cc1, cc2 = map(int, input().split())
    graph[cc1].append(cc2)
    graph[cc2].append(cc1)
cnt = 0
for i in range(1,N+1):
    if not visited[i]:
        bfs(i)
        cnt += 1
print(cnt)