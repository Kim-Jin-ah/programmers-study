def solution(s):
    alpha = ''
    answer = 0
    same = 0
    diff = 0
    
    for i in s:
        if same == 0 and diff == 0:
            alpha = i
            
        if i != alpha:
            diff += 1
        else:
            same += 1
        
        if same == diff:
            answer += 1
            same = 0
            diff = 0
    if same != 0:
        answer += 1
            
    return answer

## 풀이전략, 핵심 아이디어
# same과 diff를 0으로 초기화하는 것이 새로운 문자열로 시작한다는 의미가 핵심!
