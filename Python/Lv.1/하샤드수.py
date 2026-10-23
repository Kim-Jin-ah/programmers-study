def solution(x):
    num = 0
    for i in str(x):
        num += int(i)
    
    return x % num == 0

## 풀이전략, 핵심 아이디어
# 숫자의 각 자릿수 순회시키고 합 구한 후
# 나누어 떨어지는지 확인
# for i in str(x) 구조 기억하기
