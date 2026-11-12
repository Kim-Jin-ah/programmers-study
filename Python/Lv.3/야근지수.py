import heapq
def solution(n, works):
    if sum(works) <= n:
        return 0
    
    arr = [-work for work in works]
    heapq.heapify(arr)
    
    for _ in range(n):
        max_work = -heapq.heappop(arr)
        max_work -= 1
        heapq.heappush(arr,-max_work)
        
    return sum(work**2 for work in arr)

## 풀이전략, 핵심 아이디어
# heapq는 최소 힙이기 때문에 음수로 바꿔서 최대 힙처럼 사용
