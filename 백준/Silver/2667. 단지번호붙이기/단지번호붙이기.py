from collections import deque

dir = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def bfs(r, c):
    cnt = 1
    q = deque()
    q.append((r, c))
    arr[r][c] = 0
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dir[k][0]
            nc = c + dir[k][1]
            if 0<=nr<N and 0<=nc<N and arr[nr][nc] == 1:
                cnt += 1
                arr[nr][nc] = 0
                q.append((nr, nc))
    return cnt


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
tmp = []
for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:  # 집이라면
            tmp.append(bfs(r, c))
tmp.sort()
print(len(tmp))
for i in range(len(tmp)):
    print(tmp[i])