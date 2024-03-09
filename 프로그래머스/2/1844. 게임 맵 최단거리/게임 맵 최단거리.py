from collections import deque

dir = [[0,1], [0,-1], [1,0], [-1,0]]

def maze(r, c, arr):
    q = deque()
    q.append((r,c))
    while q:
        r,c = q.popleft()
        for k in range(4):
            nr = r + dir[k][0]
            nc = c + dir[k][1]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1:
                arr[nr][nc] = arr[r][c] + 1
                q.append((nr, nc))
    return arr


def solution(maps):
    answer = 0
    global N
    global M
    N = len(maps)
    M = len(maps[0])
    maps = maze(0, 0, maps)
    if maps[-1][-1] == 1:
        return -1
    return maps[-1][-1]