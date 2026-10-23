def solution(keymap, targets):
    answer = []
    keyword = {}
    for s in keymap:
        for i in range(len(s)):
            if s[i] not in keyword: 
                keyword[s[i]] = i+1
            else:
                keyword[s[i]] = min(keyword[s[i]], i+1)
    for target in targets:
        total = 0
        for c in target:
            if c not in keyword:
                total = -1
                break
            total += keyword[c]
        
        answer.append(total)
        
    return answer

## 풀이전략, 핵심 아이디어
# 문자를  키로, 최소 누름 횟수를 값으로 하는 딕셔너리를 만들고 시작하는 것이 포인트!
# 값을 빠르게 찾아야 할 때 딕셔너리를 떠올리기
# min(a,b) 문법 정의와 예외처리 부분에 더 신경쓰기
