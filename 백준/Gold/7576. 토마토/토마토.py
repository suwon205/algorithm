from collections import deque

dir = [(0,-1),(0,1),(1,0),(-1,0)]
q = deque()
def bfs():
    while q:
        r,c = q.popleft()
        for k in range(4):
            nr = r + dir[k][0]
            nc = c + dir[k][1]
            if 0<=nr<N and 0<=nc<M and box[nr][nc] == 0:
                box[nr][nc] = box[r][c] +1
                q.append((nr,nc))
    return
M,N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

for r in range(N):
    for c in range(M):
        if box[r][c] == 1:
            q.append((r,c))
bfs()
maxV = 0
while True:
    for row in range(N):
        if 0 in box[row]:
            print(-1)
            exit(0)
        if maxV < max(box[row]):
            maxV = max(box[row])
    print(maxV-1)
    # print('******')
    # print(maxV)
    break