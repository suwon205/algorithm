from collections import deque
def bfs(computer):
    global cnt
    q = deque()
    visited[computer] = True
    q.append(computer)
    while q:
        tmp = q.popleft()
        for k in cpt[tmp]:
            # print(cpt[tmp], visited)
            if not visited[k]:
                cnt += 1
                visited[k] = True
                q.append(k)
    return


N = int(input())
cnt = 0
pair = int(input())
cpt = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for i in range(pair):
    cp1, cp2 = map(int, input().split())
    cpt[cp1].append(cp2)
    cpt[cp2].append(cp1)
bfs(1)
print(cnt)