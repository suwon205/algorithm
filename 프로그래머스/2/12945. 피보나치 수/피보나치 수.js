function solution(n) {
    var answer = 0;
    let fibo = new Array(n + 1).fill(0);
    fibo[0] = 0
    fibo[1] = 1
    for (let i = 2; i < n + 1; i++) {
        fibo[i] = (fibo[i-1] + fibo[i-2]) % 1234567
    }
    console.log(fibo)
    return fibo[fibo.length - 1];
}