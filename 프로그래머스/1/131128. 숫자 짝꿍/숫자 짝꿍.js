function solution(X, Y) {
    let xSet = new Set(X);
    let ySet = new Set(Y);
    let commonDigits = Array.from(xSet).filter(digit => ySet.has(digit));
    // commonDigits에는 두 문자열에 공통으로 나타나는 숫자들이 배열로 저장

    if (commonDigits.length === 0) {
        return '-1';
    }
    if (commonDigits.length === 1  && commonDigits[0] === '0') {
        return '0'
    }

    commonDigits.sort((a, b) => b - a);
    let result = '';
    // 공통으로 나타나는 숫자들을 순회하면서 최소 등장 횟수만큼 추가
    for (let digit of commonDigits) {
        let countInX = X.split(digit).length - 1;  // X에서 현재 숫자가 등장하는 횟수
        let countInY = Y.split(digit).length - 1;  // Y에서 현재 숫자가 등장하는 횟수
        let minCount = Math.min(countInX, countInY);

        // 최소 등장 횟수만큼 현재 숫자를 결과 문자열에 추가
        result += digit.repeat(minCount);
    }

    return result;
}