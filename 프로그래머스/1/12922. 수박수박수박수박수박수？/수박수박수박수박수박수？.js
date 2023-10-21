function solution(n) {
    var answer = '';
    var curPrintSu = true;
    
    for (let i = 0; i < n ; i++) {
        if (curPrintSu == true) {
            answer += '수'
        } else {
            answer += '박'
        }
        curPrintSu = !curPrintSu
    }
    return answer;
}