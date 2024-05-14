function solution(s) {
    var answer = 0;
    let dic = {'(' : 0, ')' : 0, '[' : 0, ']' : 0, '{' : 0, '}' : 0}
    for (let i = 0; i < s.length; i++) {
        dic[s[i]] += 1
    }
    if (dic['('] !== dic[')'] || dic['{'] !== dic['}'] || dic['['] !== dic[']']) {
        return answer
    }
    for (let i = 0; i < s.length; i++) {
        let stack = []
        let tmp = s.slice(i) + s.slice(0,i)
        for (let idx = 0; idx < tmp.length; idx++) {
            if (tmp[0] === ')' || tmp[0] === ']' || tmp[0] === '}') {
                continue
            }
            else {
                if (idx === 0) {
                    stack.push(tmp[idx])
                } else {
                    if (tmp[idx] === '}' && stack[stack.length-1] === '{') {
                        stack.pop()
                    }
                    else if (tmp[idx] === ']' && stack[stack.length-1] === '[') {
                        stack.pop()
                    }
                    else if (tmp[idx] === ')' && stack[stack.length-1] === '(') {
                        stack.pop()
                    }
                    else {
                        stack.push(tmp[idx])
                    }
                }
            }
            // console.log(stack)
            // console.log('안임')
            if (idx === tmp.length - 1 && stack.length === 0) {
                answer += 1
            } 
        }
        // console.log(stack)
        // console.log('밖임')
        // if (stack.length === 0) {
        //     answer += 1
        // }
    }
    return answer;
}