def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    
    for ch in new_id:
        if ('a'<= ch <= 'z') or ('0'<= ch <= '9') or ch in '-_.':
            if ch == '.' and answer.endswith('.'):
                continue
            answer += ch
    
    if answer[0] == '.' or answer[-1] == '.':
        answer = answer.strip(".")
    
    if answer == '':
        answer = 'a'
        
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer.rstrip(".")
                   
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]
    
    return answer

## 풀이전략, 핵심 아이디어
# 특정 문자를 제외하는 필터링과 endswith() 활용이 핵심
# while 반복문 돌리는 것도 헷갈리지 말기
