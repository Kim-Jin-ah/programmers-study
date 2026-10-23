def solution(array, height):
    answer = 0
    for arr in array:
        if arr > height:
            answer += 1
    return answer

## 풀이전략, 핵심 아이디어
# 단순 조건문 문제
