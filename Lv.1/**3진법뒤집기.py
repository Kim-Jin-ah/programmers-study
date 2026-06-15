def solution(n):
    answer = ''
    
    while n:
        answer += str(n%3)
        n //= 3
        
    return int(answer,3)

## 풀이전략, 핵심 아이디어
# 3진법이 되는 원리 알아두어야함. 나누기 활용!!!
# 3진법에서 다시 10진법으로 int(,) 활용 기억하기
