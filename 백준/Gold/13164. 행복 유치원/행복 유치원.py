N,K = map(int, input().split())
childlist = list(map(int, input().split()))
priceList = [0] * (N-1) #이웃한 값과의 차이를 나타낼 리스트
for idx in range(N-1): #이웃 값과의 차이 구하기
    priceList[idx] = childlist[idx+1] -childlist[idx]
priceList.sort()
ans = sum(priceList[:N-K])
print(ans)
