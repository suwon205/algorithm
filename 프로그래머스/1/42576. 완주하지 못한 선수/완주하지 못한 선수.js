function solution(participant, completion) {
    participant.sort();
    completion.sort();

    for (var i = 0; i < participant.length; i++) {
        if (i === participant.length - 1 || participant[i] !== completion[i]) {
            return participant[i];
        }
    }

    return ''; // 이 부분은 실행되지 않을 것이므로 빈 문자열 반환
}
