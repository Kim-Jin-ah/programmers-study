def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n % i == 0:
            answer += i
            
    return answer

## 풀이전략, 핵심 아이디어
# 약수 구한 후, 해당되는 숫자를 더하면서 answer에 넣기
# 비교적 쉬운 문제
