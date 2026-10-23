import math
def solution(progresses, speeds):
    days = []
    
    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i])
        days.append(day)
    
    answer = []
    max_day = days[0]
    count = 0
    
    for day in days:
        if day <= max_day:
            count += 1
        else:
            answer.append(count)
            max_day = day
            count = 1
    answer.append(count)
    
    return answer

## 풀이전략, 핵심 아이디어
# 완료일을 알아내야 하므로 math.ceil()을 이용해야한다는 점 기억
# max_day를 우선 설정하고 이걸 기준으로 크기 비교하며 count가 핵심!!
