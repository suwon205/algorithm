function solution(people, limit) {
    var answer = 0;
    people.sort((a,b) => a-b)
    console.log(people)
    while (people.length > 0) {
        if (people.length >= 2 && people[0] + people[people.length - 1] <= limit) {
            answer ++;
            people.shift()
            people.pop()
        } else {
            people.pop()
            answer ++
        }
        // console.log(people)
    }
    return answer;
}