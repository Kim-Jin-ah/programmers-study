def solution(sides):
    
    return 2 * min(sides)-1

## 풀이전략, 핵심 아이디어
# 우선, 삼각형의 완성조건이  |a+b|<x<a+b 임을 기억하기
# 또한, 두 변이 주어졌을 떄 가능한 세번째 변의 개수 공식; 2*작은변 -1

# for 문으로 직접 세는 방법(참고)
def solution(sides):
    answer = 0
    a, b = sorted(sides)
    
    for x in range(abs(a - b) + 1, a + b):
        answer += 1
    
    return answer
