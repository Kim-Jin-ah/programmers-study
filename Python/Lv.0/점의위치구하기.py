def solution(dot):
    answer = 0
    if (dot[0]>0) & (dot[1] > 0):
        answer = 1
    elif (dot[0]<0) & (dot[1] > 0):
        answer = 2
    elif (dot[0]<0) & (dot[1] < 0):
        answer = 3
    elif (dot[0]>0) & (dot[1] < 0):
        answer = 4
    return answer

## 풀이전략, 핵심아이디어
# 양수와 음수인지 if문으로 확인하는 문제
