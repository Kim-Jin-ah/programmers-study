from collections import Counter
def solution(array):
    counter = Counter(array)
    max_count = max(counter.values())
    result = []
    
    for key, value in counter.items():
        if value == max_count:
            result.append(key)
    if len(result) > 1:
        return -1
    
    return result[0]

## 풀이전략, 핵심 아이디어
# 각 숫자가 몇 번 나왔는지 세기
# 가장 큰 등장 횟수 찾고, 여러개면 -1 return
# 딕셔너리 문법 적극 활용 필요
