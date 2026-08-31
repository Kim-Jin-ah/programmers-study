def solution(numbers, target):
    def dfs(index,total):
        if index == len(numbers):
            if total == target:
                return 1
            else:
                return 0
            
        plus = dfs(index+1, total + numbers[index])
        minus = dfs(index+1, total - numbers[index])
        
        return plus + minus
    
    return dfs(0,0)

## 풀이전략, 핵심 아이디어
# DFS 문제로, 재귀를 활용한 문제
# 과정이 이해가 되어야만 풀 수 있으므로, 무조건적인 암기가 아닌 원리 먼저 분석 필요
