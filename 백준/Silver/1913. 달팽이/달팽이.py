dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N = int(input())
find = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
st = N * N
row, col = 0, 0
d = 0

while st:
    arr[row][col] = st
    if st == find:
        find_row, find_col = row, col

    st -= 1
    nr = row + dir[d][0]
    nc = col + dir[d][1]

    if nr < 0 or nr >= N or nc < 0 or nc >= N or arr[nr][nc] != 0:
        d = (d + 1) % 4
        nr = row + dir[d][0]
        nc = col + dir[d][1]

    row, col = nr, nc

for a in arr:
    for i in a:
        print(i, end=' ')
    print()
print(find_row+1, find_col+1)
