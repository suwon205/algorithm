function solution(n, s, a, b, fares) {
    var answer = Number.MAX_SAFE_INTEGER; // 충분히 큰 값으로 초기화
    let INF = Number.MAX_SAFE_INTEGER; // 충분히 큰 값으로 초기화
    let graph = Array.from({length : n + 1}, () => Array(n+1).fill(INF))
    
    // 자기 자신으로의 거리는 0으로 초기화
    for (let i = 1; i < n + 1; i ++) {
        graph[i][i] = 0;
    }    
    
    // fares를 이용하여 그래프 초기화
    for (let fare of fares) {
        let v = fare[0];
        let w = fare[1];
        let pay = fare[2];
        graph[w][v] = pay;
        graph[v][w] = pay;
    }
    
    // 플로이드-와샬 알고리즘 수행하여 모든 노드 간의 최단 거리 계산
    for (let k = 1; k < n + 1; k++) {
        for (let i = 1; i < n + 1; i ++) {
            for (let j = 1; j < n + 1; j++) {
                graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]);
            }
        }
    }
    
    // 각 지점을 경유하여 최소 요금 계산
    for (let i = 1; i < n + 1; i++) {
        answer = Math.min(answer, graph[s][i] + graph[i][a] + graph[i][b]);
    }
    
    return answer;
}
