def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x

def union(x,y):
    rep[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    rep = [i for i in range(N)]
    lst = []
    for _ in range(M):
        p1, p2 = map(int, input().split())
        union(p1-1,p2-1)
    ans = []
    for r in rep:
        ans.append(find_set(r))
    print(f'#{tc} {len(set(ans))}')