def solution(word):
    vowels = ["A","E","I","O","U"]
    count = 0
    answer = 0
    
    def dfs(current):
        nonlocal count, answer
        
        if current == word:
            answer = count
            return
        if len(current) == 5:
            return
        for v in vowels:
            count += 1
            dfs(current + v)
            
            if answer != 0:
                return
    dfs("")
    
    return answer

## 풀이전략, 핵심 아이디어
# 재귀DFS를 이해하지 못하면 풀지 못하는 문제
# dfs의 과정을 이해하고 외우기 + 백트래킹
