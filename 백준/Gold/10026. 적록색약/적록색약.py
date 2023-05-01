from collections import deque

dir = [(0,-1),(0,1),(-1,0),(1,0)]

def bfs(r,c):
    q = deque()
    q.append((r,c))
    visited[r][c] = True
    while q:
        r,c = q.popleft()

        for k in range(4):
            nr = dir[k][0] + r
            nc = dir[k][1] + c
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
                if arr[r][c] == arr[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr,nc))

N = int(input())
arr = [list(input()) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
abnormal = normal = 0
for r in range(N):
    for c in range(N):
        if visited[r][c] == False:
            bfs(r,c)
            normal += 1
for r in range(N):
    for c in range(N):
        if arr[r][c] == 'R':
            arr[r][c] = 'G'
visited = [[False]*N for _ in range(N)]

for r in range(N):
    for c in range(N):
        if visited[r][c] == False:
            bfs(r,c)
            abnormal += 1

print(normal, abnormal)