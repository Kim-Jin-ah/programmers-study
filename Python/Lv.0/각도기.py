def solution(angle):
    answer = 0
    if angle< 90:
        return 1
    elif angle == 90:
        return 2
    elif angle <180:
        return 3
    else:
        return 4
        
    return answer

## 풀이전략, 핵심 아이디어
# if 조건문만 잘 적으면 되는 문제
