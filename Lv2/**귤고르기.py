from collections import Counter
def solution(k, tangerine):
    count = Counter(tangerine)
    count = sorted(count.values(),reverse=True)
    
    answer = 0
    for num in count:
        k -= num
        answer += 1
        
        if k <= 0:
            break
        
    return answer

## 풀이전략, 핵심 아이디어
# 종류의 개수를 최소화하면서 k개 고르기
# 각 종류의 개수를 Counter로 세고, 개수가 많은 순서대로 정렬 후
# 큰 것부터 빼면서 몇 종류가 필요한지 센다.
