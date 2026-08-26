def solution(n):
    if n == 1:
        return 1
    
    a = 1
    b = 2
    
    for i in range(3,n+1):
        a,b = b, a+b
        
    return b % 1234567

## 풀이전략, 핵심 아이디어
# 피보나치 수열 활용하기
# 예외처리 신경쓰기
