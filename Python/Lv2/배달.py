import heapq
def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    distance = [float('inf')] * (N+1)
    distance[1] = 0
    
    heap = [(0,1)]
    while heap:
        time,now = heapq.heappop(heap)
        
        if time > distance[now]:
            continue
        for next_node,cost in graph[now]:
            new = time + cost
            
            if new < distance[next_node]:
                distance[next_node] = new
                heapq.heappush(heap,(new,next_node))
    
    answer = 0
    for i in range(1,N+1):
        if distance[i] <= K:
            answer += 1
            
    return answer

## 풀이전략, 핵심 아이디어
# 1번 마을에서 각 마을까지의 최단거리를 구하고, 그 최단거리가 K 이하인 마을의 개수 세기
# 각 번호의 거리를 저장하는 graph를 만들어 최단거리가 나올때마다 갱신하여 저장 이 핵심
