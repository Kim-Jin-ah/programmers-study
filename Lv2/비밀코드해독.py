from itertools import combinations
def solution(n, q, ans):
    answer = 0
    for com in combinations(range(1,n+1),5):
        q_set = set(com)
        
        is_vaild = True
        for i in range(len(q)):
            count = len(q_set.intersection(q[i]))
            
            if count != ans[i]:
                is_vaild = False
                break
                
        if is_vaild:
            answer += 1
            
    return answer

## 풀이전략, 핵심 아이디어
# set()을 활용하여 교집합을 구하고 true,false로 정답 판별
