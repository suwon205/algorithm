def solution(n, s, a, b, fares):
    # 노드의 수 n, 시작 지점 s, 내릴 지점 a, 내릴 지점 b, 요금 표 fares
    INF = int(1e9)  # 무한을 의미하는 값으로 충분히 큰 값으로 초기화
    answer = INF
    
    # 각 노드 간의 거리를 저장할 2차원 배열 초기화
    graph = [[INF] * (n+1) for _ in range(n+1)]
    # 자기 자신으로의 거리는 0으로 초기화
    for i in range(1, n+1):
        graph[i][i] = 0
    
    # 요금 표 fares에 있는 정보로 각 노드 간의 거리 업데이트
    for fare in fares:
        u, v, w = fare
        graph[u][v] = w
        graph[v][u] = w
    
    # 플로이드-와샬 알고리즘 수행
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    # 모든 경우에 대해 최소 요금 계산
    for i in range(1, n+1):
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])
    
    return answer
