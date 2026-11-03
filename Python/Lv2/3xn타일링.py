def solution(n):
    if n % 2 == 1:
        return 0
    
    dp = [0] * (n+1)
    
    dp[0] = 1
    dp[2] = 3
    
    for i in range(4,n+1,2):
        dp[i] = (4 * dp[i-2] - dp[i-4])
        
    return dp[n] % 1000000007

## 풀이전략, 핵심 아이디어
# 홀수 처리를 우선적으로 하고
# 4부터 n까지 짝수만 순회하며 점화식 사용
