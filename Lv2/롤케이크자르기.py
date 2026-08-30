from collections import Counter
def solution(topping):
    answer = 0
    
    left = set()
    right = Counter(topping)
    
    for i in range(len(topping)-1):
        left.add(topping[i])
        
        right[topping[i]] -= 1
        
        if right[topping[i]] == 0:
            del right[topping[i]]
        if len(left) == len(right):
            answer += 1
    return answer

## 풀이전략, 핵심 아이디어
# 반복문 안에서 같은 데이터를 계속 처음부터 다시 계산하지 말고, 이전 계산 결과를 유지하면서 조금씩 업데이트하는 방식으로 계산
