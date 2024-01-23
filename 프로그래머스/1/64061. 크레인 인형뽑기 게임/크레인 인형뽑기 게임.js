function solution(board, moves) {
    var answer = 0;
    console.log(board)
    stacklist = []
    
    for (const move of moves){
        for (idx = 0; idx < board.length; idx++) {
            if (board[idx][move-1] != 0) {
                if (stacklist.length >= 1 && stacklist[stacklist.length-1] == board[idx][move-1]) {
                    answer += 2
                    stacklist.pop()
                }
                else{
                    stacklist.push(board[idx][move-1])
                }
                board[idx][move-1] = 0
                break
            }
        }
    }    
    return answer;
}