import heapq
def solution(n, k, enemy):
    heap = []
    for i in range(len(enemy)):
        heapq.heappush(heap,enemy[i])
        
        if len(heap) > k:
            n -= heapq.heappop(heap)
        
        if n < 0:
            return i
        
    return len(enemy)

## 풀이전략, 핵심 아이디어
# 반복문에서 순서대로 heap애 넣으면서
# '지금까지 중 무적권을 사용할 k개의 후보' 관리
# k를 초과하면 가장 작은 적을 n으로 막는다
