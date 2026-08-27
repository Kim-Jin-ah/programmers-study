from itertools import permutations
def solution(k, dungeons):
    answer = 0
    
    for i in permutations(dungeons):
        count = 0
        total = k
        
        for j in i:
            mini = j[0]
            consume = j[1]
            
            if total >= mini:
                total -= consume
                count += 1
            else:
                break
        answer = max(answer,count)
    return answer

## 풀이전략, 핵심 아이디어
# 순서에 따라 결과가 달라지고, 가능한 경우의 수가 많지 않다면 '완전탐색' 의심해보기
# 던전 순서를 전부 만들고 각 순서마다 현재 피로도로 입장 가능한지 확인 후 조건문으로 확인 -> 가장 많이 방문한 횟수 저장 후 return
