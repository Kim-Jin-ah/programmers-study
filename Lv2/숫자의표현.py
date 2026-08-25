def solution(n):
    answer = 0
    m = n // 2
    for i in range(1,m+1):
        total = 0
        for j in range(i,n+1):
            total += j
            
            if total == n:
                answer += 1
                break
            if total > n:
                break
                
    return answer + 1

## 풀이전략, 핵심 아이디어
# 코드를 한번에 구상하는 게 좀 어려웠음 -> 이중 반복문 활용법 익히기
# 시작 숫자를 하나 정하고, 그 숫자부터 계속 더해보는 과정이 포인트
