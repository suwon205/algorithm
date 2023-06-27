from collections import deque

N, K = map(int, input().split())
visited = [-1] * 100001  # 방문한 위치를 저장하는 배열
route = []

def bfs(start, target):
    q = deque()
    q.append((start, 0))
    visited[start] = start

    while q:
        cur, curtime = q.popleft()

        if cur == target:
            idx = cur
            while idx != start:
                route.append(idx)
                idx = visited[idx]
            route.append(start)
            return curtime

        for next_pos in [cur + 1, cur - 1, cur * 2]:
            if 0 <= next_pos <= 100000 and visited[next_pos] == -1:
                q.append((next_pos, curtime + 1))
                visited[next_pos] = cur

print(bfs(N, K))
print(*route[::-1])
