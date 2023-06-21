from collections import deque

N, K = map(int, input().split())

MAX_SIZE = 100000

q = deque([N])
visit = [False] * (MAX_SIZE + 1)
visit[N] = True
cnt = 0

while q:
    level = len(q)  # 현재 단계에서 큐에 추가된 노드 수
    for _ in range(level):
        cur = q.popleft()
        if cur == K:
            print(cnt)
            exit()
        for next_node in (cur + 1, cur * 2, cur - 1):
            if 0 <= next_node <= MAX_SIZE and not visit[next_node]:
                q.append(next_node)
                visit[next_node] = True
    cnt += 1
