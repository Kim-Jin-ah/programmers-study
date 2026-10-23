def solution(n):
    answer = []
    for i in str(n):
        answer.append(int(i))
    answer.reverse()
    
    return answer

## 풀이전략, 핵심 아이디어
# 뒤집는 방법 : reverse() 또는 [::-1] 이해하기
# [::-1]을 사용한 방법
def solution(n):
    answer = []
    for i in str(n)[::-1]:
        answer.append(int(i))
    return answer
  
# map을 사용한 다른 방법
def solution(n):
    return list(map(int, str(n)[::-1]))
