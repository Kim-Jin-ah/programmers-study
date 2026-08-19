import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    
    count = 0
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        new = first + second*2
        heapq.heappush(scoville,new)
        
        count += 1
    return count

## 풀이전략, 핵심 아이디어
# 힙 이해하기!(import heapq) + 힙 함수 익히기
# 계속 작은 값을 꺼내야 할 때 사용 용이
# 예외 처리 까먹지 말고 신경쓰기
