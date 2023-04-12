N = int(input())
triangle = [list(map(int,input().split())) for _ in range(N)]

#목표는 그때그때 작은 것을 찾아서 저장해주는 것. (행+1, 열)과 (행+1, 열+1) 중에서 큰 값 찾기!
#삼각형의 제일 왼쪽과 오른쪽은 특수하게 처리해주어야 한다. max값을 사용해서 비교하지 않는다.
r = 0
c = 0
sumV = triangle[r][c]

for i in range(1,N): #행
    for j in range(len(triangle[i])): #열
        if j == 0: #맨 왼쪽에 있는 경우
            triangle[i][j] = triangle[i][j] + triangle[i-1][0]
        elif j == len(triangle[i])-1: #맨 오른쪽에 있는 경우
            triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
        else:
            triangle[i][j] = max(triangle[i][j] + triangle[i-1][j], triangle[i][j]+triangle[i-1][j-1])
print(max(triangle[N-1]))