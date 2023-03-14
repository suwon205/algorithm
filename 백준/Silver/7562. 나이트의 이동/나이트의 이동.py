from collections import deque
import sys

input = sys.stdin.readline
# 방문한 곳을 1로 표시할 것. 0으로 표시되고 + 나이트의 이동 범위라면 움직일 것

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, -2, -1, 1, 2]


def bfs(x, y, wx, wy):
    q = deque()
    q.append((x, y))
    chess[x][y] = 1

    while q:
        x, y = q.popleft()
        if x == wx and y == wy:
            print(chess[x][y]-1)
            return
        else:
            for k in range(8):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0<=nx<l and 0<=ny<l and chess[nx][ny] == 0:
                    q.append((nx,ny))
                    chess[nx][ny] = chess[x][y]+1

T = int(input())
for _ in range(T):
    l = int(input())
    chess = [[0] * l for _ in range(l)]
    x, y = map(int, input().split())
    want_x, want_y = map(int, input().split())
    chess[x][y] = 1
    bfs(x, y, want_x, want_y)