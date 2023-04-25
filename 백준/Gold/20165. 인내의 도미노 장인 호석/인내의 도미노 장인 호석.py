def func(r,c,dir,l):
    global tmp
    if arr[r][c] >= 1: #높이가 1 이상이라면
        arr[r][c] = 0 #쓰러진다
        tmp += 1
    for _ in range(l-1): #도미노 길이 -1만큼 반복
        r += dir_dict[dir][0]
        c += dir_dict[dir][1]
        if 0<=r<N and 0<=c<M:
            func(r,c,dir,arr[r][c])
N,M,R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
copy_arr = [row[:] for row in arr]
answer= 0
for _ in range(R):
    att_r, att_c, att_dir = input().split()
    def_r, def_c = map(int,input().split())
    att_r = int(att_r) -1
    att_c = int(att_c) -1
    def_r -= 1
    def_c -= 1
    dir_dict = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}

    #공격
    tmp = 0
    if arr[att_r][att_c]:
        func(att_r, att_c, att_dir, arr[att_r][att_c])
    #수비
    arr[def_r][def_c] = copy_arr[def_r][def_c]
    answer += tmp
print(answer)
for r in range(N):
    for c in range(M):
        if arr[r][c]:
            arr[r][c] = "S"
        else:
            arr[r][c] = "F"

    print(*arr[r])