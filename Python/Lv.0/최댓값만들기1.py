def solution(numbers):
    answer = 0
    numbers.sort()
    answer = numbers[-1]*numbers[-2]
    return answer

## 풀이전략, 핵심 아이디어
# 정렬!!! 활용!! 기억하기!!!!!...
