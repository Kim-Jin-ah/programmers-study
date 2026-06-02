def solution(n):

    for i in range(2,n):
        if n % i == 1:
            return i

## 풀이전략, 핵심 아이디어
# 반복문의 범위를 (2,n) 으로
# 1과 n은 검사할 필요가 없기 때문
