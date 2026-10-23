def solution(array, n):
    answer = 0
    for arr in array:
        if arr == n:
            answer += 1
    return answer

## 풀이전략, 핵심 아이디어
# 같은지 비교 + 조건문 활용
