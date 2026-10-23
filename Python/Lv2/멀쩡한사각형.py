import math
def solution(w,h):
    total_squares = w * h
    unusable_squares = w + h - math.gcd(w, h)
    
    return total_squares - unusable_squares

## 풀이전략, 핵심 아이디어
# 사용할 수 없는 사각형의 개수 = 대각선이 지나가는 사각형의 개수 공식 임
# 따라서, 공식을 알면 바로 풀 수 있는 문제,,
