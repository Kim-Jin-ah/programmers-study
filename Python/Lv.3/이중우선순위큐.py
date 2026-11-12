import heapq
def solution(operations):
    answer = []
    arr = []
    
    for op in operations:
        if "I" in op:
            op = op.replace("I ","")
            heapq.heappush(arr,int(op))            
        elif op == "D -1":
            if not arr:
                continue
            else:
                heapq.heappop(arr)
        elif op == "D 1":
            if not arr:
                continue
            else:
                minus = [-num for num in arr]
                heapq.heapify(minus)
                                
                heapq.heappop(minus)

                arr = [-n for n in minus]
                heapq.heapify(arr)

    if not arr:
        return [0,0]
    else:
        return [max(arr),min(arr)]
# 힙 하나 사용한 방법

import heapq
def solution(operations):
    min_heap = []
    max_heap = []
    count = {}
    
    for operation in operations:
        command,value = operation.split()
        value = int(value)
        
        if command == "I":
            heapq.heappush(min_heap,value)
            heapq.heappush(max_heap,-value)
            count[value] = count.get(value,0) + 1
        
        elif command == "D":
            if value == 1:
                while max_heap and count.get(-max_heap[0],0) == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    max_value = -heapq.heappop(max_heap)
                    count[max_value] -= 1

            elif value == -1:
                while min_heap and count.get(min_heap[0],0) == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    min_value = heapq.heappop(min_heap)
                    count[min_value] -= 1
    
    while min_heap and count.get(min_heap[0],0) == 0:
        heapq.heappop(min_heap)
    
    while max_heap and count.get(-max_heap[0],0) == 0:
        heapq.heappop(max_heap)
    
    if not min_heap:
        return [0,0]

    return [-max_heap[0],min_heap[0]]
# 힙 두개 사용한 방법
  
## 풀이전략, 핵심 아이디어
# min_heap은 원래 숫자를 넣어 최솟값 삭제
# max_heap은 숫자에 -를 붙여 최댓값 삭제
# 효율적으로 힙 두개가 더 나은 방법임
