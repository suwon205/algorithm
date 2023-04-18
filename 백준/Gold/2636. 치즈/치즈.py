#접근 로직: bfs로 사방탐색을 하면서... bfs를 한 번 돌 때마다 공기와 접촉한 부분은 녹았다고 처리해주기
# 치즈를 1, 공기를 0으로 할 것.
# 외부 공기와 맞닿은 치즈는 일반적인 치즈와 구별해주기 위해 2로 설정했다.
from collections import deque

dir = [(0,1),(0,-1),(-1,0),(1,0)]

def bfs():
    cnt = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append((0,0))
    visited[0][0] = True
    while q:
        r,c = q.popleft()

        for k in range(4):
            nr = r + dir[k][0]
            nc = c + dir[k][1]
            if 0<=nr<N and 0<=nc<M and not visited[nr][nc]: #외부 공기와 맞닿은 치즈의 경우
                if cheese[nr][nc] == 1: #치즈인 경우
                    visited[nr][nc] = True
                    cheese[nr][nc] = 0 # 녹았다!
                    cnt += 1
                else:
                    visited[nr][nc] = True
                    q.append((nr,nc))
    ans.append(cnt)
    return cnt
N,M = map(int,input().split())
cheese = [list(map(int,input().split())) for _ in range(N)] #패딩을 대줘서... 외부 공기와 맞닿은 부분을 구해줄까?
time =0
ans =[]
while True:
    time += 1
    cnt = bfs()
    if cnt == 0:
        break
print(time-1)
print(ans[time-2])