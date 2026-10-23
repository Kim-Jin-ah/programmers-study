def solution(num):
    count = 0
    while num != 1:
        if num % 2 == 0:
            num //= 2
            
        else:
            num = num * 3 + 1
            
        count += 1
        
        if count == 500:
            return -1
    
    return count

## 풀이전략, 핵심 아이디어
# 몇 번 반복할지 모르기 때문에 while 이용
# 조건문 사용하여 개수 세기
