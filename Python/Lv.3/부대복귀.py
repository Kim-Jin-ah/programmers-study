from collections import deque
def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n+1)]
    
    for a,b in roads:
        graph[a].append(b)
        graph[b].append(a)
        
    dist = [-1] * (n+1)
    dist[destination] = 0
    
    queue = deque([destination])
    while queue:
        now = queue.popleft()
        
        for next_node in graph[now]:
            if dist[next_node] == -1:
                dist[next_node] = dist[now] + 1
                queue.append(next_node)
                
    return [dist[s] for s in sources]

## 풀이전략, 핵심 아이디어
# 각 source마다 bfs를 실행하면 효율x
# 양방향 그래프이므로 목적지에서 출발해도 각 출발지까지의 거리를 구할 수 있음을 활용
