def solution(n):
    answer = []
    
    for i in range(1, n+1):
        if n % i == 0:
            answer.append(i)
            
    return answer

## 풀이전략, 핵심아이디어
# 약수니까 범위는 1~n까지
# 하나씩 대입해서 나누어떨어지면 append로 결과에 추가
