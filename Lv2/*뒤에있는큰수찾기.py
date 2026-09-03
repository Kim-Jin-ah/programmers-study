def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            index = stack.pop()
            answer[index] = numbers[i]

        stack.append(i)

    return answer

## 풀이전략, 핵심 아이디어
# 현재 숫자가 스택에 있는 숫자보다 크다면, 현재 숫자가 그 숫자의 "뒤에 있는 큰 수" 가 된다는 과정 이해하기
# 이 문제에서의 pop()의 역할 -> 큰 수를 찾았으므로 더 이상 스택에서 기다릴 필요가 없기 때문
# 따라서, 스택에 아직 뒤의 큰 수를 찾지 못한 숫자들의 인덱스만 남아있을 수 있도록.
