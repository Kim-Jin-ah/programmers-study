def solution(str1, str2):
    answer = 0
    if str2 in str1:
        return 1
    else:
        return 2
    return answer

## 풀이전략, 핵심 아이디어
# in 연산자만 알면 쉽게 풀 수 있는 문제
# find(),count()의 방법도 있음. 다음 복습 때 시도해보기
