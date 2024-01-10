from collections import deque

dir = [[0, 1], [0, -1], [-1, 0], [1, 0]]

def bfs(r, c):
    q = deque()
    q.append((r, c))
    cnt = 1  # cnt를 1로 초기화
    houses[r][c] = 0  # 방문한 집을 0으로 표시
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dir[k][0]
            nc = c + dir[k][1]
            if 0 <= nr < N and 0 <= nc < N and houses[nr][nc]:
                houses[nr][nc] = 0
                cnt += 1
                q.append((nr, nc))
    return cnt

N = int(input())
houses = [list(map(int, input())) for _ in range(N)]
cntDanzi = 0
cntHouse = []
for r in range(N):
    for c in range(N):
        if houses[r][c]:
            cntHouse.append(bfs(r, c))
            cntDanzi += 1
print(cntDanzi)
cntHouse.sort()
for i in cntHouse:
    print(i)
