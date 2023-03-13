from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, -2, -1, 1, 2]


def bfs(arr, x, y, fx, fy):
    q = deque()
    q.append((x, y))
    arr[x][y] = 1
    while q:
        x, y = q.popleft()
        if x == fx and y == fy:
            print(arr[fx][fy]-1)
            return
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < l and 0 <= ny < l and arr[nx][ny] == 0:
                q.append((nx, ny))
                arr[nx][ny] = arr[x][y] +1

T = int(input())
for _ in range(T):
    l = int(input())
    cnt = 0
    arr = [[0] * l for _ in range(l)]
    x, y = map(int, input().split())
    fx, fy = map(int, input().split())
    arr[x][y] = 1
    bfs(arr, x, y, fx, fy)