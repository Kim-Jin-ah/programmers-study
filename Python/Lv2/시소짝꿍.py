from collections import Counter
def solution(weights):
    count = Counter(weights)
    answer = 0
    
    for w,n in count.items():
        answer += n * (n-1) // 2
        
        for a,b in [(2,1),(3,2),(4,3)]:
            if w * a % b == 0:
                other = w * a // b
                
                if other > w and other in count:
                    answer += n * count[other]
                    
    return answer

## 풀이전략, 핵심 아이디어
# 각각의 몸무게 개수를 구하고, 짝꿍이 될 수 있는 4가지 몸무게를 찾기
# 해시를 사용하여 빠른 탐색. 시간 효율 신경쓰기
