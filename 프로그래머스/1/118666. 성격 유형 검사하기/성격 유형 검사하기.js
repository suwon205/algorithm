function solution(survey, choices) {
    var answer = '';
    var dic = {'R' : 0, 'T': 0, 'C' : 0, 'F': 0, 'J': 0, 'M' : 0, 'A' : 0, 'N' : 0}
    
    // survay 순회하며 choice에 따른 점수 올려주어야 한다.
    
    for (var idx = 0; idx < choices.length; idx++) {
        if (choices[idx] > 4) {
            dic[survey[idx][1]] += choices[idx] - 4
        } else if (choices[idx] < 4) {
            dic[survey[idx][0]] += 4 - choices[idx]
        }
    }
    console.log(dic)
    if (dic['R'] < dic['T']) {
        answer += 'T'
    } else {
        answer += 'R'
    }
    if (dic['C'] < dic['F']) {
        answer += 'F'
    } else {
        answer += 'C'
    }
    if (dic['J'] < dic['M']) {
        answer += 'M'
    } else {
        answer += 'J'
    }
    if (dic['A'] < dic['N']) {
        answer += 'N'
    } else {
        answer += 'A'
    }
    return answer;
}