from collections import Counter
def solution(want, number, discount):
    dic = {}
    for w in range(len(want)):
        dic[want[w]] = number[w]
    
    count = 0
    for i in range(len(discount)-9):
        total = Counter(discount[i:i+10])
        if dic == total:
            count += 1
            
    return count

## 풀이전략, 핵심 아이디어
# 원하는 상품의 개수를 저장하고 10개씩 확인, 상품 종류와 개수 비교 순서로 진행
# Counter를 제대로 활용할 수 있다면 쉽게 풀 수 있는 문제
