def solution(schedules, timelogs, startday):
    answer = 0
    day = {1:(5,6),2:(4,5),3:(3,4),4:(2,3),5:(1,2),6:(0,1),7:(0,6)}
    sday = day[startday]
    
    for i in range(len(schedules)):
        sh = schedules[i]
        
        sh += 10
        if sh % 100 >= 60:
            sh += 40
            
        success = True
        
        for t in range(7):
            if t == sday[0] or t == sday[1]:
                continue
                
            if timelogs[i][t] > sh:
                success = False
                break
        
        if success:
            answer += 1
            
    return answer

## 풀이전략, 핵심 아이디어
# 반복문의 대상(직원->요일) 의 형태 파악이 핵심
# 시간 변환 방식을 문제에 특화된 구현이 아닌 방법으로도 풀어보기
