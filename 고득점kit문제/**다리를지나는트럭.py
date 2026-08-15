from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    
    time = 0
    current_weight = 0
    
    while trucks or current_weight > 0:
        out = bridge.popleft()
        current_weight -= out
        
        if trucks and current_weight + trucks[0] <= weight:
            truck = trucks.popleft()
            bridge.append(truck)
            current_weight += truck
        else:
            bridge.append(0)
        
        time += 1
            
    return time  

## 풀이전략, 핵심 아이디어
# bridge를 실제 다리 길이만큼의 큐로 만들어서 1초마다 한 칸씩 이동시킨다 가 핵심!
# queue를 두개 만들어서 서로 빼는 것과 추가하는 응용
