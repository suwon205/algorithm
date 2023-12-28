function convertToBin(n, char) {
    var bin = char.toString(2)
    while (bin.length != n) {
        bin = '0' + bin;
    }
    return bin
}

function assembleMap(n, numMap1, numMap2) {
    var secretMap = [];
    
    for (let i = 0; i < n; i++) {
        var inputText = "";
        for (let j = 0; j < n; j++) {
            if (numMap1[i][j] == 1 || numMap2[i][j] == 1) {
                inputText += "#";
            } else {
                inputText += " ";
            }
        }
        secretMap.push(inputText)
    }
    return secretMap;
}

function solution(n, arr1, arr2) {
    var answer = [];
    var temp1 = [];
    var temp2 = [];
    for (let i = 0; i < n; i++) {
        temp1.push(convertToBin(n, arr1[i]))
        temp2.push(convertToBin(n, arr2[i]))
    }
    return assembleMap(n, temp1, temp2);
}