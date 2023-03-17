import sys
input = sys.stdin.readline
from collections import deque

q = deque()
dir = [(0, -1), (0, 1), (1, 0), (-1, 0)]

def bfs():
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dir[k][0]
            ny = y + dir[k][1]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] +1
                q.append((nx, ny))

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            q.append((r,c))
res = 0
bfs()
#sumV 합을 구한다.
for i in arr:
    for k in i:
        if k == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res-1)