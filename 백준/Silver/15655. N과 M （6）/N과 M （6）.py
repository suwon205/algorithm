from itertools import combinations

N,M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
for j in combinations(lst, M):
    for idx in range(M):
        print(j[idx], end=' ')
    print()