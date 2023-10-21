function solution(n) {
    var answer = -1;
    var transformNumber = Math.sqrt(n)
    if (Math.floor(transformNumber) == transformNumber) {
        return (transformNumber +1 ) ** 2
    }
    return answer;
}