let dir = [[0,1],[0,-1],[1,0],[-1,0]]; // 방향을 나타내는 요소는 음수일 수 있으므로 []로 묶어줍니다.

function bfs(r, c, maps) {
    let N = maps.length;
    let M = maps[0].length;
    let dq = [];
    dq.push([r, c]); // 변경된 부분: 요소를 []로 묶어줍니다.
    while (dq.length > 0) { // 변경된 부분: while 조건을 dq.length > 0으로 수정합니다.
        [r, c] = dq.shift(); // 변경된 부분: 요소를 []로 묶어줍니다.
        for (let k = 0; k < 4; k++) {
            let nr = r + dir[k][0];
            let nc = c + dir[k][1];
            if (0 <= nr && nr < N && 0 <= nc && nc < M && maps[nr] && maps[nr][nc] === 1) { // maps[nr]이 undefined가 아닌지 확인
                maps[nr][nc] += maps[r][c];
                dq.push([nr, nc]); // 변경된 부분: 요소를 []로 묶어줍니다.
            }
        }
    }
    return maps;
}

function solution(maps) {
    var answer = 0;
    bfs(0, 0, maps);
    // console.log(maps[maps.length-1][maps[0].length-1])
    if (maps[maps.length-1][maps[0].length-1] === 1) {
        return -1
    }
    return maps[maps.length-1][maps[0].length-1];
}
