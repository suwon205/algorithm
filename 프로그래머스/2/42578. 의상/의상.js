function solution(clothes) {
    dic = {}
    for (cloth of clothes) {
        if (dic[cloth[1]]) {
            dic[cloth[1]] += 1
        } else {
            dic[cloth[1]] = 1
        }
    }
    console.log(dic)
    var answer = 1;
    for (cnt in dic) {
        answer *= (dic[cnt] + 1)
    }
    return answer - 1;
}