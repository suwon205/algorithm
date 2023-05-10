def DP(v):
    sub = [] # 노드 v를 루트로 하는 서브트리를 도는 동안 걸리는 최소 시간 구하는 리스트
    for i in TREE[v]:
        DP(i)
        sub.append(time[i])
    if not time[v]: #말단까지 온 경우!
        sub.append(0)
    sub.sort(reverse=True)
    tmp_time = [sub[i] + i + 1 for i in range(len(sub))]
    time[v] = max(tmp_time)
N = int(input())
tmp = list(map(int, input().split()))
TREE = [[] for _ in range(N)]
for i in range(1,N):
    TREE[tmp[i]].append(i)
time = [False] * N
DP(0)
print(time[0]-1)