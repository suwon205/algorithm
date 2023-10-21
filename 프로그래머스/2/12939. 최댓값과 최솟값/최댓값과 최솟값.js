function solution(s) {
    var answer = '';
    var tempList = []
    var numStr = String(s).split(' ');
    for(let i = 0; i < numStr.length; i++) {
        console.log(numStr[i])
        if (!isNaN(numStr[i])) {
            tempList.push(parseInt(numStr[i]))
        }
    }
    answer += Math.min(...tempList)
    answer += ' '
    answer += Math.max(...tempList)
    console.log(tempList)
    return answer;
}