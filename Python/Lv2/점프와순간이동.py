def solution(n):
    ans = 0

    while n >= 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n-1) // 2
            ans += 1
            
    return ans

## 풀이전략, 핵심 아이디어
# 목표에서 거꾸로 내려오면서 문제에 접근하기
# 홀짝 판별과 몫 구하기 활용 문제
