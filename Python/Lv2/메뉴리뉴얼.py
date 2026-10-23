from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for c in course:
        counter = Counter()
        for order in orders:
            order = sorted(order)
            for comb in combinations(order,c):
                menu = ''.join(comb)
                counter[menu] += 1
                
        if counter:
            max_count = max(counter.values())
            if max_count >= 2:
                for menu,count in counter.items():
                    if count == max_count:
                        answer.append(menu)
    return sorted(answer)

## 풀이전략, 핵심 아이디어
# 메뉴조합 만들고, 조합별 등장 횟수를 세어 가장 많이 나온 횟수를 찾아 리턴하는 것이 핵심
# combinations를 사용해 조합을 뽑고 join으로 합치기, Counter로 그 조합의 등장횟수를 세고 max 찾기
