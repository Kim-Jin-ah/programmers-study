from collections import deque
def solution(land):
    n = len(land)
    m = len(land[0])
    visited = [[False]*m for _ in range(n)]
    dic = {}
    group_id = 2
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    
    def bfs(x,y,num):
        queue = deque([(x,y)])
        visited[x][y] = True
        land[x][y] = num
        count = 1
        
        while queue:
            x,y = queue.popleft()
            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and land[nx][ny] == 1:
                        visited[nx][ny] = True
                        land[nx][ny] = num
                        queue.append((nx,ny))
                        count += 1
        return count
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                size = bfs(i,j,group_id)
                dic[group_id] = size
                group_id += 1
                
    max_oil = 0
    for c in range(m):
        current = 0
        seen_groups = set()
        for r in range(n):
            if land[r][c] > 1:
                num = land[r][c]
                seen_groups.add(num)
        
        for num in seen_groups:
            current += dic[num]
        
        max_oil = max(max_oil,current)
        
    return max_oil

## 풀이전략, 핵심 아이디어
# deque를 활용한 문제... bfs 활용 신경쓰기
