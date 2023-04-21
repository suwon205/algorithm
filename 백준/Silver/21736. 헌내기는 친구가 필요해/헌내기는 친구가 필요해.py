from collections import deque

dir = [(0,1),(0,-1),(-1,0),(1,0)]

def bfs(r,c):
    cnt = 0
    q = deque()
    q.append((r,c))
    while q:
        r,c = q.popleft()
        for k in range(4):
            nr = r + dir[k][0]
            nc = c + dir[k][1]
            if 0<=nr<N and 0<=nc<M: #범위 안에 든다면
                if arr[nr][nc] == 'O':
                    q.append((nr,nc))
                    arr[nr][nc] = 'X'
                elif arr[nr][nc] == 'P':
                    cnt += 1
                    arr[nr][nc] = 'X'
                    q.append((nr,nc))
    return cnt

N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
cnt = 0
for r in range(N):
    for c in range(M):
        if arr[r][c] == 'I':
            ans = bfs(r,c)
if ans == 0:
    print('TT')
else:
    print(ans)