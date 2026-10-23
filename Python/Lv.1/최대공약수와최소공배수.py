import math
def solution(n, m):
    
    gcd = math.gcd(n,m)
    lcm = n*m / gcd
    
    return [gcd,lcm]

## 풀이 전략, 핵심 아이디어
# 최대공약수 함수 이용하기, 최소공배수 공식 암기하기

# 직접 구하는 방식으로는
def solution(n, m):

    gcd = 1

    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            gcd = i

    lcm = n * m // gcd

    return [gcd, lcm]
