def solution(n):
    answer = 1
    for i in range(1,n+1):
        answer *= i
        
        if answer > n:
            return i-1
    return answer

## 풀이전략, 핵심아이디어
# 팩토리얼 구하는 문제 + 가장 큰 i 찾기
# 팩토리얼은 반복문으로
# i를 찾는건 if문으로 구하기
