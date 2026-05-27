def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n % i == 0:
            answer += 1
    return answer

## 풀이전략, 핵심 아이디어
# 약수의 개수 구하기와 매우 유사한 문제
# 공식 외우자..
