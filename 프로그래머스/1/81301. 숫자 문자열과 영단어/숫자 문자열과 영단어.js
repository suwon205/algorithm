function solution(s) {
    // 숫자에 대응되는 영단어와 그에 해당하는 숫자를 매핑
    const wordToNumber = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    };

    let result = "";
    let temp = "";

    for (let i = 0; i < s.length; i++) {
        if (isNaN(s[i])) {
            // 문자가 숫자가 아니면 temp에 추가
            temp += s[i];
            if (wordToNumber[temp] !== undefined) {
                // temp가 숫자에 해당하는 영단어인 경우, 숫자로 변환하여 result에 추가
                result += wordToNumber[temp];
                temp = ""; // temp 초기화
            }
        } else {
            // 문자가 숫자인 경우, 그대로 result에 추가
            result += s[i];
        }
    }

    return parseInt(result, 10); // 결과 문자열을 숫자로 변환하여 반환
}
