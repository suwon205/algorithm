from collections import deque
dir = [(0,1),(0,-1),(-1,0),(1,0)]

def area(r,c):
    q = deque()
    visited[r][c] = True
    q.append((r,c))
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dir[k][0]
            nc = c + dir[k][1]
            if 0 <= nr < N and 0<= nc < N and not visited[nr][nc] and pic[nr][nc] == pic[r][c]:
                visited[nr][nc] = True
                q.append((nr, nc))
    return

N = int(input())
pic = [list(input()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
nor_cnt = ab_cnt = 0
# 비장애인의 경우
for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            area(r,c)
            nor_cnt += 1
# 그림 바꾸기
for r in range(N):
    for c in range(N):
        if pic[r][c] == 'R':
            pic[r][c] = 'G'

visited = [[False] * N for _ in range(N)]
#색맹의 경우
for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            area(r,c)
            ab_cnt += 1

print(nor_cnt, ab_cnt)