function solution(numbers) {
    let answer = Array(numbers.length).fill(-1);
    let stack = [];
    
    numbers.forEach((num, idx) => {
        while (stack.length > 0 && num > numbers[stack[stack.length - 1]]) {
            answer[stack.pop()] = num
        }
        stack.push(idx)
    })

    return answer;
}