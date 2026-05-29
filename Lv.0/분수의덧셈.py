import math
def solution(numer1, denom1, numer2, denom2):
    
    numer = numer1*denom2 + numer2*denom1
    denom = denom1*denom2
    
    gcd = math.gcd(numer,denom)
    
    return [numer // gcd, denom // gcd]

## 풀이전략, 핵심 아이디어
# 분모가 같도록 분자,분모를 만들고 덧셈을 한 다음 최대공약수로 나누기
