def DP(v):
    child = []
    for idx in tree[v]:
        DP(idx) #제일 끝까지 들어가기...
        child.append(time[idx])
    if not time[v]:
        child.append(0)
    child.sort(reverse=True) #시간이 많이 걸리는 사람부터 볼 것
    nTime = [child[i] + i +1 for i in range(len(child))]
    time[v] = max(nTime)
N = int(input())
tree = [[] for _ in range(N)]
lst = list(map(int, input().split()))
for idx in range(1,N):
    tree[lst[idx]].append(idx)
time = [False] * N

DP(0)
print(time[0]-1)