function solution(N, stages) {
    var answer = [];
    var challenge = {}; // 도전했지만 실패한 단계 기록
    var clear = {}; // 성공한 단계 기록
    var clearPercent = [];
    
    // 각 스테이지에 대한 도전 횟수 초기화
    for (var idx = 1; idx <= N + 1; idx++) {
        challenge[idx] = 0;
    }    
    // 플레이어가 도전한 스테이지에 대해 처리
    for (var i = 0; i < stages.length; i++) {
        var stage = stages[i];
        for (var idx = 1; idx <= stage; idx++) {
            challenge[idx] += 1;
        }
    }
    
    // 각 스테이지에 대한 클리어 플레이어 수 계산
    for (var idx = 1; idx <= N; idx++) {
        clear[idx] = challenge[idx] - challenge[idx + 1];
    }
    
    for (var idx = 1; idx <= N; idx++) {
        if (clear[idx] === 0) {
            answer.push([0, idx]);
        } else {
            answer.push([clear[idx] / challenge[idx], idx]);
        }
    }
    
    answer.sort((a, b) => {
        // 첫번째 요소를 내림차순으로 정렬
        if (b[0] - a[0] !== 0) {
            return b[0] - a[0];
        }
        // 첫번째 요소가 같은 경우 두번째 요소를 오름차순으로 정렬
        return a[1] - b[1];
    });

    console.log(answer);
    for (i = 0; i < N; i++) {
        clearPercent.push(answer[i][1])
    }
    return clearPercent;
}

// 예시로 호출
solution(5, [2, 1, 2, 6, 2, 4, 3, 3]);
