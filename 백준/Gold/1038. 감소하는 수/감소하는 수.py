from itertools import combinations

N = int(input())

res = []
for i in range(1,11):
    for j in combinations(range(10),i):
        j = j[::-1]
        num = ''.join(list(map(str, j)))
        res.append(int(num))
res.sort()
if len(res) > N: #N번째 감소하는 수가 존재한다면!
    print(res[N])
else:
    print(-1) #존재하지 않다면!
    
#누구보다 조합 만들고 싶어... 왜 안 만들어져...