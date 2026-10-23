def solution(s):
    stack = []
    
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    
    if len(stack) == 0:
        return 1
    else:
        return 0

  ## 풀이전략, 핵심 아이디어
  # 스택을 활용하여 푸는 문제 - 뒤에서 빼면서 비교하고, 추가해야하는 문제는 스택활용하기!!
