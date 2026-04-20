def solution(n):
    answer = 0
    for i in range(1,1001):
        if i * i == n:
            return 1
    return 2

## 풀이전략, 핵심아이디어
# if 문 안에 return 2를 넣으면 안돼
# 밖에 있어야 모두 반복함. 안그러면 1번째 반복 후 종료됨

# 다음 복습 땐 import math로 수학 라이브러리를 가져와 실행시켜보기
