from collections import deque
import sys
input = sys.stdin.readline

dx = [0,0,1,-1,1,1,-1,-1]
dy = [1,-1,0,0,-1,1,-1,1]

def bfs(ls, x, y):
    q = deque()
    if ls[x][y] == 1:
        q.append((x,y))
        ls[x][y] = 0

        while q:
            x,y = q.popleft()
            for k in range(8):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0<=nx<h and 0<=ny<w:
                    if ls[nx][ny] == 1:
                        ls[nx][ny] = 0
                        q.append((nx,ny))
        return

while True:
    w,h = map(int, input().split())
    cnt = 0
    if w == 0 and h == 0:
        break
    else:
        ls =[]
        for _ in range(h):
            ls.append(list(map(int,input().split())))
    for r in range(h):
        for c in range(w):
            if ls[r][c] == 1:
                bfs(ls, r, c)
                cnt += 1
    print(cnt)