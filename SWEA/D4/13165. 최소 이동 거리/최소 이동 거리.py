def dijkstra(s, V):  # 출발, 마지막 정점 번호
    U = [0] * (V+1)# U는 최소 비용이 결정된 정점의 집합
    U[s] = 1 # U = {s}에 해당.
    for i in range(V+1): #s에서 정점 i로 가는 비용
        D[i] = adjM[s][i]
    #남은 정점의 비용 결정
    # while U!=w:
    N = V+1
    for _ in range(N-1): # N-1개의 비용 결정
        #D[w]가 최소인 w 결정
        minV = INF
        w = 0
        for i in range(V+1):
            if U[i] == 0 and minV > D[i]: # 비용이 결정되지 않은 상태 + 남은 정점 i 중 최소를 찾기
                w = i
                minV = D[i]
        U[w] = 1 # 최소인 w는 최소 비용 D[w] 확정됨을 의미

        #w에 인접인 정점에 대해 기존 비용 VS w를 거쳐가는 비용을 비교
        for v in range(V+1):
            if 0 < adjM[w][v] < INF: # w에 인접한 v의 조건
                D[v] = min(D[v], D[w] + adjM[w][v])


T = int(input())
for tc in range(1,T+1):
    INF = 10  # 문제에 따라
    N, E = map(int, input().split())  # 0~V번 정점, E는 간선 수
    adjM = [[INF] * (N + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        adjM[i][i] = 0  # 자기자신으로 가는 비용

    for _ in range(E):
        u, v, w = map(int, input().split())  # u -> v로 가는 비용은 w(가중치)
        adjM[u][v] = w

    D = [0] * (N + 1)

    dijkstra(0,N)
    print(f'#{tc} {D[N]}')
# print(D)