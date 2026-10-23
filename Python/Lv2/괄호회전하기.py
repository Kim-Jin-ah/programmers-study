def solution(s):
    answer = 0
    
    for i in range(len(s)):
        rotated = s[i:] + s[:i]
        stack = []
        
        for char in rotated:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    break
                    
                if (stack[-1] == '(' and char == ')') or (stack[-1] == '[' and char == ']') or (stack[-1] == '{' and char == '}'):
                    stack.pop()
                else:
                    break
        else:
            if not stack:
                answer += 1
                
    return answer

## 풀이전략, 핵심 아이디어
# for-else 활용(break 없이 반복문이 끝까지 실행됐을 때 else 실행)
# 문자열 회전 -> 스택으로 괄호 검사 -> 올바르면 answer + 1
