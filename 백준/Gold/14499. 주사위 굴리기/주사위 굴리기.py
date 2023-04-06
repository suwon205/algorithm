diceidx = [0]*6
direc = [(0,1),(0,-1),(-1,0),(1,0)]

def dice(dir):
    a,b,c,d,e,f =diceidx[0],diceidx[1],diceidx[2],diceidx[3],diceidx[4],diceidx[5]
    if dir == 1: #동
        diceidx[0],diceidx[1],diceidx[2],diceidx[3],diceidx[4],diceidx[5] = d,b,a,f,e,c
    if dir == 2: #서
        diceidx[0],diceidx[1],diceidx[2],diceidx[3],diceidx[4],diceidx[5] = c,b,f,a,e,d
    if dir == 3: #북
        diceidx[0],diceidx[1],diceidx[2],diceidx[3],diceidx[4],diceidx[5] = e,a,c,d,f,b
    if dir == 4:
        diceidx[0],diceidx[1],diceidx[2],diceidx[3],diceidx[4],diceidx[5] = b,f,c,d,a,e


N,M,x,y,K = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(N)]
prompts = list(map(int,input().split()))
nx = x
ny = y
for prompt in prompts:
    nx += direc[prompt-1][0]
    ny += direc[prompt-1][1]
    if 0>nx or N<=nx or 0>ny or M<=ny: #해당 명령 무시와 출력 무시 코드
        nx -= direc[prompt-1][0]
        ny -= direc[prompt-1][1] #이전으로 되돌려주기
        continue
    dice(prompt)
    if map_list[nx][ny] == 0:
        map_list[nx][ny] = diceidx[-1]
    else: #이동하는 칸이 0이 아닌 경우
        diceidx[-1] = map_list[nx][ny]
        map_list[nx][ny] = 0
    print(diceidx[0])
#어디가 문제지?