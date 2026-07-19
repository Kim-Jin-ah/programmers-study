from collections import Counter
def solution(X, Y):
    cx = Counter(X)
    cy = Counter(Y)
    answer = []
    
    for i in range(9,-1,-1):
        num = str(i)
        answer.append(num * min(cx[num],cy[num]))
    answer = "".join(answer)
    
    if answer == "":
        return "-1"
    if answer[0] == "0":
        return "0"
    return answer

## 풀이전략, 핵심 아이디어
# counter 함수 적용 및 min 활용
# 반복문 내 구조 기억해두기
# 추가로 검사해야하는 것들 if문으로 필터링 잊지말기
