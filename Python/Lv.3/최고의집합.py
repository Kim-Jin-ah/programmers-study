def solution(n, s):
    answer = []

    if n > s:
        return [-1]
    
    a = s // n
    b = s % n
    
    answer = [a] * (n-b) + [a+1] * b
            
    return answer

## 풀이전략, 핵심 아이디어
# 모든 원소가 최대한 비슷한 값을 가질 때 곱이 최대가 된다 가 핵심
# 수학적 규칙 이용
