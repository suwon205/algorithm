from collections import deque
import copy
dir = [(0,-1),(0,1),(-1,0),(1,0)]

def bfs():
    q = deque()
    sample = copy.deepcopy(arr)
    for i in range(N):
        for j in range(M):
            if sample[i][j] == 2:
                q.append((i,j))
    while q:
        r,c = q.popleft()
        for k in range(4):
            nr = r + dir[k][0]
            nc = c + dir[k][1]
            if 0<=nr<N and 0<=nc<M:
                if sample[nr][nc] == 0:
                    sample[nr][nc] = 2
                    q.append((nr,nc))
    global res
    cnt = 0
    for i in range(N):
        for k in range(M):
            if sample[i][k] == 0:
                cnt += 1
    res.append(cnt)


def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(cnt+1)
                arr[i][j] = 0

N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
res = []
wall(0)
print(max(res))