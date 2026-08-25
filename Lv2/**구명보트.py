def solution(people, limit):
    people.sort()
    
    left = 0
    right = len(people) - 1
    
    answer = 0
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            
        right -= 1
        answer += 1
        
    return answer

## 풀이전략, 핵심 아이디아
# 가장 무거운 사람을 기준으로 가장 가벼운 사람을 붙여보는 방식 활용
# 투 포인터 사용 방식 기억하기
