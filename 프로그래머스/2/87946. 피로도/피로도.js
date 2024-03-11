function solution(k, dungeons) {
    var answer = 0;
    let visited = new Array(dungeons.length).fill(false);
    
    function dfs(curHP, cnt) {
        
        for (let i = 0; i < dungeons.length; i ++) {
            if (curHP >= dungeons[i][0] && !visited[i]) {
                visited[i] = true
                dfs(curHP - dungeons[i][1], cnt + 1)
                visited[i] = false
            }
        }
        
        answer = Math.max(answer, cnt)
    }
    
    dfs(k, 0);
    return answer;
}
