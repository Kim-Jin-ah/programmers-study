from collections import deque
def solution(board):
    n = len(board)
    m = len(board[0])
    
    start = None
    target = None
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                start = (i,j)
    
    queue = deque()
    queue.append(start)
    arr = [[-1]*m for _ in range(n)]
    arr[start[0]][start[1]] = 0
    directions = [(0,1),(1,0),(-1,0),(0,-1)]
    
    while queue:
        x,y = queue.popleft()
        
        if board[x][y] == "G":
            return arr[x][y]
        
        for dx,dy in directions:
            nx = x
            ny = y
            
            while True:
                next_x = nx + dx
                next_y = ny + dy
            
                if (next_x < 0 or next_x >= n or next_y <0 or next_y >= m or board[next_x][next_y] == "D"):
                    break
                nx = next_x
                ny = next_y
                
            if nx == x and ny == y:
                continue
            
            if arr[nx][ny] == -1:
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx, ny))
                
    return -1

## 풀이전략, 핵심 아이디어
# 현재 로봇 위치를 하나 꺼내고, 네 방향 각각 확인 -> 한 번 이동할 떄 while True:를 이용해 벽/장애물까지 계속 이동하게 함 -> arr에 횟수 저장
