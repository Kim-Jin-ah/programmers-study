from itertools import permutations
def solution(numbers):
    num = set()
    n = 1
    while n <= len(numbers):
        for i in permutations(numbers,n):
            num.add(i)
        n += 1
    
    arr = set()
    for i in num:
        joinstr = ''.join(i)
        if joinstr.startswith("0"):
            continue
        arr.add(joinstr)
            
    count = 0
    for i in arr:
        prime = True
        num = int(i)
        if num < 2:
            prime = False
            continue
        for j in range(2,int(num**0.5)+1):
            if num % j == 0:
                prime = False
                break
        if prime:
            count += 1
        
    return count

from itertools import permutations
def solution(numbers):
    answer = set()
    
    for i in range(1,len(numbers)+1):
        for p in permutations(numbers,i):
            num = int("".join(p))
            if num < 2:
                continue
                
            for j in range(2,int(num**0.5)+1):
                if num % j == 0:
                    break
            else:
                answer.add(num)
    return len(answer)

## 풀이전략, 핵심 아이디어
# 메모리적으로 더 좋은 방법, 깔끔하게 풀 수 있는 방법 연구하고, 그런식으로 문제 풀어보기
# 한번에 배열을 만들어가는 게 메모리적으로나 보기에나 좋기 때문에 아래 방법 선호
