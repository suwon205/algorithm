from collections import deque
dir = [(0,-1),(0,1),(-1,0),(1,0)]
def bfs():
    D = [[1e10] * N for _ in range(N)]
    Q = deque()
    Q.append((0,0))
    D[0][0] = 0

    while Q:
        r,c = Q.popleft()
        for k in range(4):
            nr = r + dir[k][0]
            nc = c + dir[k][1]
            if 0<=nr<N and 0<=nc<N:
                gap = max(0,arr[nr][nc])
                if D[nr][nc] > D[r][c] + gap:
                    D[nr][nc] = min(D[nr][nc], D[r][c] + gap)
                    Q.append((nr,nc))
    return D[N-1][N-1]
T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    print(f'#{tc} {bfs()}')