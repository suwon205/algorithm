from collections import deque
import sys
input = sys.stdin.readline

dir = [(-2,-1),(-1,-2),(1,2),(2,1),(-1,2),(1,-2),(2,-1),(-2,1)]

def bfs(r,c):
    global cnt
    q = deque()
    q.append((r,c))
    arr[r][c] = 0 #이동한 지점 -1로 표시하자

    while q:
        r,c = q.popleft()
        if r==want_r and c==want_c:
            print(arr[want_r][want_c])
            return
        for k in range(8):
            nr = r + dir[k][0]
            nc = c + dir[k][1]
            if 0<=nr<l and 0<=nc<l:
                if arr[nr][nc] == 0:
                    arr[nr][nc] += arr[r][c] +1
                    q.append((nr,nc))
    print(arr[want_r][want_c])
    return
T = int(input())
for _ in range(T):
    cnt = 0
    l = int(input())
    arr = [[0 for _ in range(l)] for _ in range(l)]
    cur_r, cur_c = map(int, input().split())
    want_r, want_c = map(int, input().split())
    bfs(cur_r,cur_c)