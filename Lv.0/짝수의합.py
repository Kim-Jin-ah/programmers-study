def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        if i % 2 == 0:
            answer += i
    return answer

## 풀이전략, 핵심 아이디어
# 범위는 1부터 n까지, 짝수만 더하기
# %2 활용!
