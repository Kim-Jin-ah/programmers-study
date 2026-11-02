def solution(info, n, m):
    INF = float('inf')
    
    dp = [INF] * m
    dp[0] = 0
    
    for a,b in info:
        next_dp = [INF] * m
        
        for j in range(m):
            if dp[j] == INF:
                continue
                
            if dp[j] + a < n:
                next_dp[j] = min(next_dp[j],dp[j] + a)
            if j + b < m:
                next_dp[j+b] = min(next_dp[j+b],dp[j])
        dp = next_dp
    
    answer = min(dp)
    
    if answer == INF:
        return -1
    
    return answer

## 풀이전략, 핵심 아이디어
# 과정을 이해하는 것이 관건. dp 사용 문제
# B의 흔적 제약(m)을 인덱스로 활용
# A의 흔적 제약(n) 조기 검사
