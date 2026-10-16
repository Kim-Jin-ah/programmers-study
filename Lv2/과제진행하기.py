def solution(plans):
    timeline = []
    for name,start,during in plans:
        h,m = map(int,start.split(":"))
        start_time = h*60 + m
        timeline.append([name,start_time,int(during)])
    timeline.sort(key=lambda x:x[1])
    
    answer = []
    stack = []
    current = 0
    for i in range(len(timeline)):
        name,start,play = timeline[i]
        
        while stack and current < start:
            p_name,p_time = stack.pop()
            if current + p_time <= start:
                current += p_time
                answer.append(p_name)
            else:
                p_time -= (start - current)
                stack.append([p_name,p_time])
                current = start
                break
        
        current = start
        
        if i == len(timeline) - 1:
            answer.append(name)
            current += play
            break
        
        next_start = timeline[i+1][1]
        if current + play <= next_start:
            current += play
            answer.append(name)
        else:
            left = play - (next_start - current)
            stack.append([name,left])
            current = next_start
            
    while stack:
        p_name,p_time = stack.pop()
        answer.append(p_name)
        
    return answer

## 풀이전략, 핵심 아이디어
# LIFO, stack 구조 활용 문제
# 시간 데이터 변환, 시간순 정렬, 스택활용하여 처리 순으로 진행
