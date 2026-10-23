from math import gcd
def lcm(a,b):
    return a*b // gcd(a,b)

def solution(signals):
    total = 1
    for g,y,r in signals:
        total = lcm(total,g+y+r)
        
    for t in range(1,total+1):
        yellow = True
        for g,y,r in signals:
            cycle = g+y+r
            pos = (t-1) % cycle
            
            if not (g<=pos<g+y):
                yellow = False
                break
        if yellow:
            return t
        
    return -1

## 풀이전략, 핵심 아이디어
# 주기적으로 반복되는 상태는 "현재시간 % 주기"로 계산!!
# 여러 주기가 동시에 반복되므로 최소공배수 활용!
