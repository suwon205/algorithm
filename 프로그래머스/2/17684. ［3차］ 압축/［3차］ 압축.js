function solution(msg) {
    var answer = [];
    dic = {};
    for (let index = 1; index <= 26; index++) {
        let letter = String.fromCharCode(index + 64);
        dic[letter] = index;
    }
    let st = 0;
    let ed = 1;
    let lastVal = 27;
    
    while (ed <= msg.length) {
        let curWord = msg.slice(st, ed)
        let newWord = msg.slice(st, ed + 1)
        
        if (newWord in dic) {
            ed += 1
        } else {
            answer.push(dic[curWord])
            dic[newWord] = lastVal;
            lastVal += 1
            st = ed
            ed += 1
        }
    }
    answer.push(dic[msg.slice(st, ed)])

    return answer;
}