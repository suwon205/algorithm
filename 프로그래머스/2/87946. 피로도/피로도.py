def solution(k, dungeons):
    visited = [False] * len(dungeons)
    def dfs(curHp, cnt):
        if cnt < len(dungeons):
            max_cnt = cnt
            for idx in range(len(dungeons)):
                if curHp >= dungeons[idx][0] and not visited[idx]:
                    visited[idx] = True
                    max_cnt = max(max_cnt, dfs(curHp - dungeons[idx][1], cnt + 1))
                    visited[idx] = False
            return max_cnt
        return cnt
    
    return dfs(k,0)
