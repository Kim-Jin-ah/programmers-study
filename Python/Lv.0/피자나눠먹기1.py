def solution(n):
    
    if n < 7:
        return 1
    else:
        if n % 7 == 0:
            return n // 7
        else:
            return (n // 7) + 1

## 풀이전략, 핵심 아이디어
# 이렇게 풀어도 되지만,,, import math 적극 활용 필요,,,
import math
def solution(n):
    return math.ceil(n / 7)
