def solution(numbers):
    numbers.sort()
    
    return max(
                numbers[0] * numbers[1],
                numbers[-1] * numbers[-2]
                )

## 풀이전략, 핵심 아이디어
# sort() 이용!!!!
# 가장 작은 음수 2개, 가장 큰 양수 2개 곱한 것 중에 큰 것 골라내면 돼
