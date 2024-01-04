n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]

for r in range(1, n):
    for c in range(r+1):
        if c == 0:
            tri[r][c] += tri[r-1][0]
        elif c == r:
            tri[r][c] += tri[r-1][c-1]
        else:
            tri[r][c] += max(tri[r-1][c], tri[r-1][c-1])
print(max(tri[-1]))