function solution(n) {
    var answer = 0;
    
    var tempLength = String(n).length;
    for (let i = 0; i < tempLength; i++) {
        answer += parseInt(String(n)[i]);
    }

    return answer;
}
