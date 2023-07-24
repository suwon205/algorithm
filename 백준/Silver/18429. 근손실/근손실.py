def backtracking(depth, tmp):
    global cnt
    if depth == N:
        cnt += 1
        return
    for i in range(N):
        if visited[i] or tmp + lst[i] - K < 0:
            continue
        visited[i] = True
        backtracking(depth+1, tmp + lst[i]-K)
        visited[i] = False

answer = []
cnt = 0
N, K = map(int, input().split())
visited = [False] * N
lst = list(map(int, input().split()))
lst.sort()
backtracking(0, 0)
print(cnt)