from math import factorial
def solution(n, k):
    people = list(range(1,n+1))
    answer = []
    
    k -= 1
    
    for i in range(n,0,-1):
        fact = factorial(i-1)
        
        index = k // fact
        
        answer.append(people.pop(index))
        
        k %= fact
    
    return answer

## 풀이전략, 핵심 아이디어
# 몫과 나머지를 활용해 해당 순서를 알아내기
# 순서대로 들어갈 숫자를 선택하는 과정 이해하기
