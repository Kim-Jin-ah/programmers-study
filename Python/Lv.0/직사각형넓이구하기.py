def solution(dots):
    answer = 0
    x =[]
    y =[]
    
    for dot in dots:
        x.append(dot[0])
        y.append(dot[1])
        
    width = max(x) - min(x)
    height = max(y) - min(y)
    answer = width * height
    
    return answer

## 풀이전략, 핵심 아이디어
# x좌표 길이, y좌표 길이를 위하기 위해
# for문 돌리고 max,min 사용
# 최대 - 최소 가 길이임을 주의
