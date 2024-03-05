function solution(priorities, location) {
    var answer = 0;
    let queue = [];
    for (let i = 0; i < priorities.length; i ++) {
        queue.push([i, priorities[i]])
    }
    let temp = [];
    while (queue.length > 0) {
        measureMax = [...queue]
        measureMax.sort((a, b) => b[1] - a[1]); // 우선 순위가 높은 것부터 정렬
        let maxVal = measureMax[0][1]
        if (maxVal === queue[0][1]) {
            answer += 1
            if (queue[0][0] === location) {
                break
            }
            queue.shift()
        } else {
        queue.push((queue.shift()))
    }
        
    } 
    console.log(queue)
    return answer;
}