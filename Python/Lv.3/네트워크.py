def solution(n, computers):
    visited = [False] * n
    answer = 0
    
    def dfs(start):
        visited[start] = True
        
        for i in range(n):
            if computers[start][i] == 1 and not visited[i]:
                dfs(i)
                
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
            
    return answer

## 풀이전략, 핵심 아이디어
# dfs 한 번 실행 -> 연결된 네트워크 하나 탐색
# dfs가 끝날 때 answer += 1 -> 네트워크 개수 하나 증가
