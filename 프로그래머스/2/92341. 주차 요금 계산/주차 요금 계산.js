

function solution(fees, records) {
    let answer = [];
    let dic = {}
    for (record of records) {
        let [time, car, info] = record.split(' ')
        if (!(car in dic)) {
            dic[car] = {"IN" : [], "OUT" : []}
        }
        dic[car][info].push(time)
    }
    console.log(dic)
    for (d of Object.values(dic)) {
        if (d["IN"].length > d["OUT"].length) {
            d["OUT"].push("23:59")
        }
    }
    
    function calc(dic) {
        let keys = Object.keys(dic).sort();
        let sortedlst = [];
        for (let key of keys) {
            sortedlst.push(dic[key])
        }
        for (val of sortedlst) {
            // console.log(val)
            let totalTime = 0

            for (let i = 0; i < val["IN"].length; i++) {
                let inTime = val["IN"][i]
                let outTime = val["OUT"][i]

                let [inH, inM] = inTime.split(":")
                let [outH, outM] = outTime.split(":")

                totalTime += (outH - inH) * 60 + (outM - inM)
            }
            if (totalTime <= fees[0]) {
                answer.push(fees[1])
            } else {
                answer.push(fees[1] + Math.ceil((totalTime - fees[0]) / fees[2]) * fees[3])
            }
        }
    }
    
    
    calc(dic)
    
    return answer;
}