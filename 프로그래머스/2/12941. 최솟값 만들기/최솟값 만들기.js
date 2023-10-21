function solution(A, B) {
    // 배열 A는 오름차순으로, 배열 B는 내림차순으로 정렬
    A.sort((a, b) => a - b);
    B.sort((a, b) => b - a);

    var answer = 0;

    // 대응되는 원소끼리 곱하여 누적
    for (var i = 0; i < A.length; i++) {
        answer += A[i] * B[i];
    }

    return answer;
}

// 테스트 예제
var A = [1, 4, 2];
var B = [5, 4, 4];

console.log(solution(A, B)); // 29
