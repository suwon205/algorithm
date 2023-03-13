#배추의 넓이가 있으면 상하좌우를 탐색하고 bfs로 연결된 배추를 탐색할 것.
# 배추가 심어져 있는 경우 1로, 심어져 있지 않는 경우 0으로 놓고 탐색한 배추의 경우 0으로 놓을 것.
# 함수를 호출하면 cnt +1 할 것. cnt 출력으로 답 마무리
from collections import deque
import sys
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(arr, x,y):
    q = deque()
    q.append((x,y))
    arr[x][y] = 0
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = 0
                q.append((nx,ny))
    return

T = int(input())
for _ in range(T):
    n,m,k = map(int,input().split())
    arr = [[0]*(m) for _ in range(n)]
    cnt = 0
    for _ in range(k):
        x,y = map(int, input().split())
        arr[x][y] = 1
    for r in range(n):
        for c in range(m):
            if arr[r][c] == 1:
                bfs(arr, r, c)
                cnt +=1
    print(cnt)