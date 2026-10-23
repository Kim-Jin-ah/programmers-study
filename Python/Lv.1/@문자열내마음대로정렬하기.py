def solution(strings, n):

    return sorted(strings, key=lambda x:(x[n],x))

## 풀이전략, 핵심 아이디어
# 람다 함수의 원리 정확히 파악 필요
# 첫번째 값 비교, 같으면 두 번째 값 비교... 를 이용하여 같은 값 비교 해결
