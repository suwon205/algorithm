function solution(s, skip, index) {
    var answer = '';
    alphabet = new Set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    newAlpha = Array.from(alphabet).filter(char => !skip.includes(char))
    newAlpha.sort()
    
    for (idx = 0; idx < s.length; idx++) {
        newIdx = newAlpha.indexOf(s[idx]) + index
        newIdx = newIdx % newAlpha.length
        answer += newAlpha[newIdx]
    }    
    return answer;
}