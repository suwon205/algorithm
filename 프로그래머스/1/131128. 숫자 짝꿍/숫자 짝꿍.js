function solution(X, Y) {
    let xSet = new Set(X);
    let ySet = new Set(Y);
    let commonDigits = Array.from(xSet).filter(digit => ySet.has(digit));
    console.log(commonDigits)
    if (commonDigits.length === 0) {
        return '-1';
    }
    if (commonDigits.length === 1  && commonDigits[0] === '0') {
        return '0'
    }

    commonDigits.sort((a, b) => b - a);
    let result = '';

    for (let digit of commonDigits) {
        let countInX = X.split(digit).length - 1;
        let countInY = Y.split(digit).length - 1;
        let minCount = Math.min(countInX, countInY);
        result += digit.repeat(minCount);
    }

    return result;
}