def solution(a, b):
    answer = 0
    x,y = a,b
    while y:
        x,y = y,x%y
    b //= x
    
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
    return 1 if b == 1 else 2
        
    return answer

## 풀이전략, 핵심 아이디어
# 최대공약수로 약분하는 것 먼저
# 기약분수로 만든 뒤 분모의 소인수가 2와 5뿐인지 확인

# 풀이방법을 한번에 떠올리기엔 어려운 문제
# 다시 풀어보기
