from collections import deque

dir = [[0,1], [0,-1], [-1, 0], [1, 0]]

def find(r, c):
    q = deque()
    q.append([r,c])
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dir[k][0]
            nc = c + dir[k][1]
            if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] == 1:
                maze[nr][nc] += maze[r][c]
                q.append([nr, nc])
    return maze[N - 1][M - 1]

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
print(find(0,0))