from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    queue = deque()
    queue.append((0,0))
    
    while queue:
        x,y = queue.popleft()
        
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx,ny))
                    
    if maps[n-1][m-1] == 1:
        return -1
    
    return maps[n-1][m-1]

## 풀이전략, 핵심 아이디어
# BFS에서 거리 숫자가 기록되는 방식을 활용하여 풀기
# 현재 위치와 방향을 우선 설정한 후
# 현재 위치에서 갈 수 있는 곳 확인, 갈 수 있다면 queue에 넣기 순서로 진행
