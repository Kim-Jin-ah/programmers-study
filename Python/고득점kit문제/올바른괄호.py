def solution(s):
    count = 0
    
    for i in s:
        if i == "(":
            count += 1
        else:
            count -= 1
            
        if count < 0:
            return False
        
    return count == 0

## 풀이전략, 핵심 아이디어
# 여는 괄호와 닫는 괄호의 개수를 세면서, 중간에 닫는 괄호가 더 많아지는지 확인

# 스택으로 풀어보면
def solution(s):
    stack = []
    
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    
    return len(stack) == 0
