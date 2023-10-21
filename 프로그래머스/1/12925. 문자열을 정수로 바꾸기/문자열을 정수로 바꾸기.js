function solution(s) {
    var answer = '';
    var isMinus = false;
    for (let idx = 0; idx < s.length; idx ++ ) {
        if (idx == 0 && s[idx] == '-') {
            isMinus = true
        } else {
            answer += s[idx]
        }
    }
    answer = parseInt(answer)
    if (isMinus) {
        answer *= -1
    }
    return answer;
}