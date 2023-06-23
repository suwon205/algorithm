N = int(input())

triangle = [list(map(int, input().split())) for _ in range(N)]

for r in range(1,N):
    for c in range(r+1):
        if c == 0:
            triangle[r][c] = triangle[r-1][0] + triangle[r][c]
        elif c == r:
            triangle[r][c] = triangle[r-1][c-1] + triangle[r][c]
        else:
            triangle[r][c] = max(triangle[r-1][c-1], triangle[r-1][c]) + triangle[r][c]
print(max(triangle[-1]))