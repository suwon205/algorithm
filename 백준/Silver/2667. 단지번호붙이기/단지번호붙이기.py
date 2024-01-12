from collections import deque

dir = [[0,1], [0,-1], [1,0], [-1,0]]

def bfs(r, c):
    q = deque()
    q.append((r,c))
    cnt = 1
    arr[r][c] = 0

    while q:
        r,c = q.popleft()
        for k in range(4):
            nr = r + dir[k][0]
            nc = c + dir[k][1]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1:
                arr[nr][nc] = 0
                q.append((nr, nc))
                cnt += 1
    return cnt

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
total = 0
ans = []
for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            ans.append(bfs(r, c))
            total += 1
ans.sort()

print(total)
for k in ans:
    print(k)