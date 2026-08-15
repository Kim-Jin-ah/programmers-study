from collections import deque
def solution(priorities, location):
    queue = deque()
    
    for i in range(len(priorities)):
        queue.append((priorities[i],i))
        
    count = 0
    
    while queue:
        priority,index = queue.popleft()
        
        if any(priority < p for p,i in queue):
            queue.append((priority,index))
        else:
            count += 1
            
            if index == location:
                return count

## 풀이전략, 핵심 아이디어
# 실제로 어떤 순서로 큐에서 실행되는지 구하는 것이 핵심. 단순 정렬만으로는 부족하다는 걸 알아야 해!
# 정렬이 안되는 이유를 이해하는 것이 포인트
# '앞에서 꺼내기' -> '뒤로 보내기' -> '다시 앞에서 꺼내기' 순서로 진행됨을 인지해야 풀 수 있음
