def solution(a, b, n):
    answer = 0
    
    while n >= a:
        new = b * (n // a)
        answer += new
        
        n = (n % a) + new
        
    return answer

## 풀이전략, 핵심 아이디어
# 반복문 + 니눗셈 + 나머지 연산
# n = (n % a) + new 가 핵심
# while n >= a 가 헷갈림!!
# 어렵게 생각하고 겁먹지 말기..!
