def solution(elements):
    answer = set()
    n = len(elements)
    elements = elements * 2
    
    for start in range(n):
        total = 0
        for length in range(n):
            total += elements[start + length]
            answer.add(total)
            
    return len(answer)

## 풀이전략, 핵심 아이디어
# 원형 배열일 경우 *2 하고 시작
# 연속해서 더하고, 중복합 제거하는 게 핵심
# 이중 반복문에서 어떻게 진행되는지 이해하기
