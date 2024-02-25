function isAlphabet(character) {
    return /[a-zA-Z]/.test(character);
}
function intersection(arr1, arr2) {
    return Array.from(new Set(arr1.filter(item => arr2.includes(item))))
}
function union(arr1, arr2) {
    return Array.from(new Set(arr1.concat(arr2)))
}
function makeData(str) {
    let result = []
    for (let i = 0; i < str.length -1; i++) {
        if (isAlphabet(str[i]) && isAlphabet(str[i+1])) {
            result.push(str[i].toLowerCase() + str[i+1].toLowerCase())
        }
    }
    return result
}
function dataToDict(datas) {
    let dic = {}
    for (let data of datas) {
        if (data in dic) {
            dic[data] += 1
        } else {
            dic[data] = 1
        }
    }
    return dic
}
function solution(str1, str2) {
    let answer = 0;
    let data1 = makeData(str1);
    let dic1 = dataToDict(data1);
    let data2 = makeData(str2);
    let dic2 = dataToDict(data2);
    
    let unicnt = 0;
    let intercnt = 0;
    
    interList = intersection(data1, data2);
    uniList = union(data1, data2);
    if (uniList.length === 0) {
        return 65536;
    }
    for (inter of interList) {
        intercnt += Math.min(dic1[inter], dic2[inter]);
    }
    for (uni of uniList) {
        if (data1.includes(uni) && data2.includes(uni)) {
            unicnt += Math.max(dic1[uni], dic2[uni]);
        } else if (data1.includes(uni)) {
            unicnt += dic1[uni];
        } else {
            unicnt += dic2[uni];
        }
    }
    
    answer = parseInt(intercnt / unicnt * 65536);
    
    return answer;
}
