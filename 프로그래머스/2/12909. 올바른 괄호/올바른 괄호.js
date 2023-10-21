function solution(s) {
    var count = 0; // 여는 괄호를 세는 변수

    for (var idx = 0; idx < s.length; idx++) {
        if (s[idx] === "(") {
            count++;
        } else if (s[idx] === ")") {
            count--;
        }

        // 여는 괄호보다 닫는 괄호가 더 많아지면 올바르지 않은 괄호 문자열
        if (count < 0) {
            return false;
        }
    }

    // 여는 괄호와 닫는 괄호의 수가 같아야 올바른 괄호 문자열
    return count === 0;
}

// 테스트 예제
console.log(solution("()")); // true
console.log(solution("(())")); // true
console.log(solution("(()())")); // true
console.log(solution("(()())(")); // false
