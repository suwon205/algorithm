N = int(input())
road = list(map(int, input().split()))
oil_price = list(map(int, input().split()))
money = oil_price[0] * road[0] #초기 충전 값
init_cost = oil_price[0]
for idx in range(1,N-1):
    if init_cost < oil_price[idx]:
        money += init_cost * road[idx]
    else:
        money += oil_price[idx] * road[idx]
        init_cost = oil_price[idx]
print(money)
