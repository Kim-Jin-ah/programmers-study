def solution(n):
    answer = 0
    num = 0
    while answer < n:
        num += 1
        if num % 3 == 0 or '3' in str(num):
            continue
        answer += 1
    return num

## 풀이전략, 핵심 아이디어
# answer와 i 구분!!
# answer가 n에 도달할 때까지 반복문 돌리기
# 3으로 나누어지거나 3이 들어간다면
# 넘기고 +1 할 수 있도록 if문 사용
