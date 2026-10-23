import math
def solution(n):
    
    lcm = (6 * n) // math.gcd(6,n)
    
    return lcm // 6

## 풀이전략, 핵심 아이디어
# 최소공배수 개념을 정확히 알아야 풀 수 있는 문제
# 최소공배수(a,b) = (a * b) / 최대공약수(a,b)
# 여기선 피자 판 개수를 알아야하므로 //6 까지 필요
