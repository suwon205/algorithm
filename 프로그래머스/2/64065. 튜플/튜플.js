function solution(s) {
    let answer = [];
    let newDict = {};
    elements = s.slice(2, s.length-2).split('},{')
    elements = elements.map(function(element) {
        return element.split(',').map(function(num) {
            return parseInt(num);
        });
    });
    elements.sort((a,b) => a.length - b.length)
    for (let idx = 0; idx < elements.length; idx++) {
        for (let i = 0; i < elements[idx].length; i++) {
            if (elements[idx][i] in newDict) {
                newDict[elements[idx][i]] += 1
            } else{
                newDict[elements[idx][i]] = 1
            }
        }
    }
    let sortedKeys = Object.keys(newDict).sort((a, b) => newDict[b] - newDict[a]);

    for (let key of sortedKeys) {
        answer.push(parseInt(key))
    }

    return answer;
}