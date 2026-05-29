def solution(price):
    
    if price >= 500000:
        price *= 0.8
    elif price >= 300000:
        price *= 0.9
    elif price >= 100000:
        price *= 0.95
    return int(price)

## 풀이전략, 핵심 아이디어
# 큰 조건부터 검사해야하는 게 핵심!!
# 이런 경우엔 큰 범위부터 검사함을 기억하기!!!
# float가 나올 경우를 대비해 int 값을 리턴하도록 하기 주의!!
