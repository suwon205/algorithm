


function solution(word) {
    let answer = 0;
    let words = ['A', 'E', 'I', 'O', 'U'];
    let tempArr = [];
    
    function DFS(cur, depth) {
        if (depth <= 5) {
            tempArr.push(cur) // 현재 문자열을 추가

            for (let i = 0; i < words.length; i ++) {
                DFS(cur + words[i], depth + 1)
            }
        }
    }
    DFS('', 0)
    console.log(tempArr)
    answer = tempArr.indexOf(word)
    return answer;
}