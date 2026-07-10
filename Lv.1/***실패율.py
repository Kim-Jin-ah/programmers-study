def solution(N, stages):
    answer = []
    arr = []
    people = len(stages)
    
    for i in range(1,N+1):
        fail = stages.count(i)
        
        if people == 0:
            rate = 0
        else:
            rate = fail / people
        arr.append((i,rate))
        
        people -= fail
        
    arr.sort(key=lambda x:x[1],reverse=True)
    for a,b in arr:
        answer.append(a)
    return answer

## 풀이전략, 핵심 아이디어
# count(), lambda, 튜플을 리스트에 저장 후 정렬 이 가장 중요
# 특히 lambda의 경우 key=lambda x : x[1] => 튜플의 두번째값(실패율)을 기준으로 정렬하는 것이 포인트. "무엇을 기준으로 정렬할지" 잘생각하기!!

# if people == 0: => 예외처리를 위함. 까먹지 말기
# 리스트 추가할때 이중리스트 형태로 넣을 수 있음 참고!!!
