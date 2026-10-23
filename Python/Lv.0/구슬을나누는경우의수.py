import math

def solution(balls, share):
    
    return math.factorial(balls) // (math.factorial(balls-share) * math.factorial(share))

## 풀이전략, 핵심아이디어
# import math 자주 활용하기!!
# 수학적 계산이 한줄로 가능!!!!
