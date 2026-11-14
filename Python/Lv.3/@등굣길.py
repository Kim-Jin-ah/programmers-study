def solution(m, n, puddles):
    MOD = 1000000007
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[1][1] = 1
    
    for a,b in puddles:
        dp[b][a] = -1
        
    for y in range(1,n+1):
        for x in range(1,m+1):
            if dp[y][x] == -1:
                dp[y][x] = 0
                continue
            
            if x == 1 and y == 1:
                continue
                
            dp[y][x] = (dp[y-1][x] + dp[y][x-1]) % MOD
                    
    return dp[n][m]

## 풀이전략, 핵심 아이디어
# dp를 이해하기 좋은 문제 -> dp 원리 이해하자!!
# x축과 y축이 반대라는 것 조심하기
