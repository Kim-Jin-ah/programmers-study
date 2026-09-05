def solution(n, k):
    number = ''
    while n:
        number += str(n%k)
        n //= k
    number = number[::-1]
    
    answer = 0
    for i in number.split("0"):
        if i == "":
            continue
            
        i = int(i)
        if i < 2:
            continue
        
        prime = True
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                prime = False
                break
        if prime:
            answer += 1
            
    return answer

## 풀이전략, 핵심 아이디어
# 소수 판별에서 int(n**0.5)+1 사용 이유 이해하기
# 0을 기준으로 split 응용 기억하기
