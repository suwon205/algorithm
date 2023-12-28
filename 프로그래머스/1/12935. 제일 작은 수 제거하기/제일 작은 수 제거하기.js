function solution(arr) {
    var answer = [];
    var min = Math.min(...arr);
    
    // filter 함수 내부의 조건문이 올바르게 수정되었습니다.
    var removedArr = arr.filter(function(num) {
        return num !== min;
    });
    if (removedArr.length == 0) {
        return [-1];
    }
    return removedArr; // 수정: answer 대신 removedArr을 반환해야 합니다.
}

// 테스트
var result = solution([4, 2, 8, 1, 5]);
console.log(result); // 출력: [4, 2, 8, 5]
