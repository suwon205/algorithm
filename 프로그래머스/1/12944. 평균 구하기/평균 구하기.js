function solution(arr) {
    var answer = 0;
    var sum = 0;
    
    for (const number of arr) {
        sum += number;
    }
    answer = sum / arr.length
    return answer;
}