function solution(numbers, target) {
    var answer = 0;
    
    function findTarget(idx, curSum) {
        if (idx === numbers.length) {
            if (curSum === target) {
                answer++;
            }
            return;
        }
            findTarget(idx + 1, curSum + numbers[idx])
    findTarget(idx + 1, curSum - numbers[idx])
    }
    

    
    findTarget(0,0)
    
    return answer;
}