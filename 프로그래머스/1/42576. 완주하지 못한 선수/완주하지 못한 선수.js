function solution(participant, completion) {
    var answer = '';
    pDict = {}
    cDict = {}
    
    for (i = 0; i < participant.length; i++) {
        if (!(participant[i] in pDict)) {
            pDict[participant[i]] = 1
        } else {
            pDict[participant[i]] += 1
        }
    }
    
    for (i = 0; i < completion.length; i++) {
        if (!(completion[i] in cDict)) {
            cDict[completion[i]] = 1
        } else {
            cDict[completion[i]] += 1
        }
    }
    for (p in pDict) {
        if (!(p in cDict)) {
            return p
        } else {
            if (pDict[p] !== cDict[p]) {
                return p
            }
        }
    }
    return answer;
}