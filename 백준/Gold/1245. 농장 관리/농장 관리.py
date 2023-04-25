dir = [(0,1),(0,-1),(-1,0),(1,0),(1,1),(1,-1),(-1,1),(-1,-1)] #8방향 탐색

def dfs(r,c):
    global peak
    st = []
    visited[r][c] = True
    for k in range(8):
        nr = r + dir[k][0]
        nc = c + dir[k][1]
        if 0<=nr<N and 0<=nc<M:
            if arr[r][c] < arr[nr][nc]:
                peak = False
            if not visited[nr][nc] and arr[nr][nc] == arr[r][c]:
                dfs(nr,nc)

#8방향 탐색해서 봉우리 찾기
#봉우리? 같은 높이를 가지는 하나 혹은 인접한 격자... 산봉우리와 인접한 격자는 산봉우리보다 낮아야 한다.
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
cnt = 0
for r in range(N):
    for c in range(M):
        if arr[r][c] >0 and not visited[r][c]:
            peak = True
            dfs(r,c)
            if peak:
                cnt += 1
print(cnt)