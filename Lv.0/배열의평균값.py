def solution(numbers):
  return sum(numbers) / len(numbers)

## 풀이전략, 핵심 아이디어
# 합계의 개수를 나누면 평균이 나옴
# 이것도 어렵게 생각해서 반복문으로 품..
# 반복문으로 풀면
def solution(numbers):
    answer = 0
    for i in numbers:
        answer += i
        result = float(answer / len(numbers))
    return result
