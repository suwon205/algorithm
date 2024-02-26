function solution(k, tangerine) {
    let answer = 0;
    let cnt = 0;
    let tDict = {};
    for (let i = 0; i < tangerine.length; i++) {
        if (tangerine[i] in tDict) {
            tDict[tangerine[i]] += 1
        } else {
            tDict[tangerine[i]] = 1
        }
    }
    let tmp = Object.entries(tDict)
    tmp.sort((a,b) => b[1] - a[1])
    for (t of tmp) {
        if (cnt >= k) {
            break
        }
        cnt += t[1]
        answer += 1
    }
    return answer;
}