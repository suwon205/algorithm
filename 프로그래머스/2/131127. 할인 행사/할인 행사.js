function solution(want, number, discount) {
    var answer = 0;
    let dic = {};
    for (let i = 0; i < number.length; i++) {
        dic[want[i]] = number[i]
    }
    for (let day = 0; day < discount.length - 9 ; day ++) {
        let flag = true;
        let saleList = discount.slice(day, day + 10)
        for (item in dic) {
            let count = saleList.filter(saleItem => saleItem === item).length;
            if (count !== dic[item]) {
                flag = false;
                break
            }
        }
        if (flag) {
            answer+=1
        }
    }
    return answer;
}