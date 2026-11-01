from collections import defaultdict
from itertools import combinations
from bisect import bisect_left
def solution(info, query):
    answer = []
    people = defaultdict(list)
    
    for data in info:
        conditions = data.split()
        score = int(conditions[-1])
        conditions = conditions[:-1]
        
        for i in range(5):
            for comb in combinations(range(4),i):
                key = conditions[:]
                
                for idx in comb:
                    key[idx] = '-'
                    
                people[''.join(key)].append(score)
    
    for key in people:
        people[key].sort()
        
    for q in query:
        conditions = q.replace(' and ', '').split()
        score = int(conditions[-1])
        key = ''.join(conditions[:-1])
        
        scores = people[key]
        answer.append(len(scores)-bisect_left(scores,score))
                
    return answer

## 풀이전략, 핵심 아이디어
# 처음부터 모든 조건 조합을 만들어 검색할 때마다 지원자 전체를 확인할 필요가 없게 만들기
# 처음에 조금 더 많은 작업을 해서 조건별 데이터를 만들어 놓고
# 실제 검색에서는 이진 탐색으로 빠르게 답을 찾는 방식
