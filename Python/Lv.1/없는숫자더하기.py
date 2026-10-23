def solution(numbers):
    answer = 0
    
    for i in range(10):
        if i not in numbers:
            answer += i
            
    return answer

## 풀이전략, 핵심 아이디어
# for i in range(10) 이 가장 큰 포인트
# 이걸 활용한 다른 방법으로는
def solution(numbers):
  return 45 - sum(numbers)
