def solution(n):

    return int(''.join(sorted(str(n),reverse=True)))

## 풀이전략, 핵심 아이디어
# 숫자의 각 자릿수를 내림차순 정렬한 뒤 다시 정수로 만들기
