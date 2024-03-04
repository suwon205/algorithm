from collections import deque

dir = [(0,1),(0,-1),(1,0),(-1,0)]

def bfs(r,c, maps):
    cnt = 1 #이동할 수 적어주기
    limitR = len(maps)
    limitC = len(maps[0])
    # maps[r][c] = -1 #방문한 곳은 -1로 표시해주기
    queue = deque()
    queue.append((r,c))
    while queue:
        r, c = queue.popleft()
        for k in range(4):
            nr = r + dir[k][0]
            nc = c + dir[k][1]
            if 0<=nr<limitR and 0<=nc<limitC and maps[nr][nc] == 1: #이동 가능
                queue.append((nr,nc))
                maps[nr][nc] += maps[r][c] #방문함
                cnt += 1
                # print(nr, nc, maps)
        
    return maps[-1][-1]

def solution(maps):
    answer = bfs(0,0, maps)
    if answer == 1:
        return -1
    return answer
