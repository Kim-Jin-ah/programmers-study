def solution(slice, n):
    answer = 0
    if n % slice == 0:
        answer = (n // slice)
    else:
        answer = (n // slice) + 1
    return answer

## 풀이전략, 핵심 아이디어
# import math 하면 더 쉽고 간단하게 풀 수 있음
# 원리는 아니까 다음엔 import math로 바로 풀어보자
import math
def solution(slice, n):
    return math.ceil(n / slice)
