function solution(n) {
    // 숫자 n을 문자열로 변환하여 각 자릿수를 배열에 저장
    var numStr = String(n).split('');
    
    // 배열을 내림차순으로 정렬
    var sortedNumStr = numStr.sort(function(a, b) {
        return b - a;
    });
    
    // 정렬된 배열을 다시 문자열로 결합하여 정수로 변환
    var result = parseInt(sortedNumStr.join(''), 10);
    
    return result;
}
