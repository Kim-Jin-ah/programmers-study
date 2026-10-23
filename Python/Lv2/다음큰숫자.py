def solution(n):
    total = bin(n).count("1")
    
    while True:
        n += 1
        
        if bin(n).count("1") == total:
            return n

## 풀이전략, 핵심 아이디어
# 이진법을 사용하여 1의 개수를 세고, while문으로 처음부터 비교
# 항상 True인 걸 반복하기엔 while True가 적합함(answer > n보다) 참고!
