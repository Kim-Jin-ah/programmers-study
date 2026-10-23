import math
def solution(r1, r2):
    answer = 0
    for i in range(1,r2+1):
        max_y = math.floor(math.sqrt(r2*r2 - i*i))
        min_y = math.ceil(math.sqrt(max(0,r1*r1 - i*i)))
        
        answer += max_y - min_y + 1
        
    return answer*4

## 풀이전략, 핵심 아이디어
# 큰 원에 floor(), 작은 원에 ceil() 사용하여
# x를 0부터 r2까지 순회하며 각각의 개수 구하며 더하기
