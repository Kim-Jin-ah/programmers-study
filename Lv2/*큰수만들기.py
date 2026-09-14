def solution(number, k):
    stack = []
    
    for i in number:
        while stack and k > 0 and stack[-1] < i:
            stack.pop()
            k -= 1
        
        stack.append(i)
    
    if k > 0:
        stack = stack[:-k]
        
    return ''.join(stack)

## 풀이전략, 핵심 아이디어
# 숫자를 앞에서부터 스택에 넣고, 숫자 비교 후 제거 횟수가 남아있다면 뒤에서부터 자른다. 그 후 join으로 문자열로 만들어 리턴하기
