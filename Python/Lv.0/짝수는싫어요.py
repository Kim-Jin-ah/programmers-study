def solution(n):
    answer = []
    for i in range(1,n+1):
        if i % 2 != 0:
            answer.append(i)
    return answer

## 풀이전략, 핵심 아이디어
# 나머지가 있는 n 이하 값들만 넣기 공식
