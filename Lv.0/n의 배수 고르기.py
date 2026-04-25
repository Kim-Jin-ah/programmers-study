def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n == 0:
            answer.append(i)      
    return answer

## 풀이전략, 핵심아이디어
# list에서 하나씩 꺼내 if로 대조해본 뒤
# 맞다면 답에 넣고 아니면 버리기
