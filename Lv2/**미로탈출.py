from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
                
    def bfs(start,target):
        queue = deque([start])
        arr = [[-1]*m for _ in range(n)]
        
        x,y = start
        arr[x][y] = 0
        
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        
        while queue:
            x,y = queue.popleft()
            
            if (x,y) == target:
                return arr[x][y]
            
            for dx,dy in directions:
                nx = x + dx
                ny = y + dy
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if maps[nx][ny] == 'X':
                    continue
                if arr[nx][ny] != -1:
                    continue

                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx,ny))
        return -1
        
    start = None
    lever = None
    exit = None
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                start = (i,j)
            elif maps[i][j] == "L":
                lever = (i,j)
            elif maps[i][j] == "E":
                exit = (i,j)
                
    to_lever = bfs(start,lever)
    
    if to_lever == -1:
        return -1

    to_exit = bfs(lever, exit)

    if to_exit == -1:
        return -1

    return to_lever + to_exit

## 풀이전략, 핵심 아이디어
# 시작 지점, lever 지점, exit 지점 간의 구간을 나누어서 두번 진행하므로 def bfs(,)를 만들어서 진행
# count를 직접 세는 대신 한 지점을 지나가면 +1 되는 방식으로 숫자 셈
