function isAlphabet(char) {
    return /^[a-zA-Z]$/.test(char);
}

function solution(s) {
    var answer = '';
    var wordList = s.split(' ');

    for (let wordIdx = 0; wordIdx < wordList.length; wordIdx++) {
        for (let letterIdx = 0; letterIdx < wordList[wordIdx].length; letterIdx++) {
            if (letterIdx === 0 && isAlphabet(wordList[wordIdx][letterIdx])) {
                answer += wordList[wordIdx][letterIdx].toUpperCase();
            } else if (isAlphabet(wordList[wordIdx][letterIdx])) {
               answer += wordList[wordIdx][letterIdx].toLowerCase()
            } else {
               answer += wordList[wordIdx][letterIdx]
            }
        }
        if (wordIdx != wordList.length-1) {
            answer += ' '
        }
    }

    return answer;
}

var input = "hello world";
console.log(solution(input)); // "HW"
