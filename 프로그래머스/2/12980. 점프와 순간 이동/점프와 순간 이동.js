function solution(n)
{
    // 거리가 홀수인 경우 무조건 순간이동이 필요함
    // n이 0이 될 때까지...
    var ans = 0; // 1부터 출발하는 것이라고 생각하자
    while (n !== 0) {
        if (n % 2 === 0) {
            n = n / 2;
        } else {
            n --;
            ans ++
        }
    }
    return ans;
}