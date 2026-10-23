from collections import deque
def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    board = [['0']*(m+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(m):
            board[i+1][j+1] = storage[i][j]
    
    def update_outside():
        queue = deque([(0,0)])
        visited = [[False]*(m+2) for _ in range(n+2)]
        visited[0][0] = True
        
        while queue:
            x,y = queue.popleft()
            for dx,dy in directions:
                nx,ny = x+dx, y+dy
                if 0 <= nx < n+2 and 0 <= ny < m+2 and not visited[nx][ny]:
                    if board[nx][ny] == '0' or board[nx][ny] == '':
                        visited[nx][ny] = True
                        board[nx][ny] = '0'
                        queue.append((nx,ny))
    update_outside()
    
    for request in requests:
        target = request[0]
        if len(request) == 1:
            to_remove = []
            for i in range(1,n+1):
                for j in range(1,m+1):
                    if board[i][j] == target:
                        for dx,dy in directions:
                            if board[i+dx][j+dy] == '0':
                                to_remove.append((i,j))
                                break
            for x,y in to_remove:
                board[x][y] = ''
            # if to_remove:
            #     update_outside()
        else:
            for i in range(1,n+1):
                for j in range(1,m+1):
                    if board[i][j] == target:
                        board[i][j] = ''
            update_outside()
    answer = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if board[i][j] != '0' and board[i][j] != '':
                answer += 1
    return answer

## 풀이전략, 핵심 아이디어
# 방문한 것과 안한것 구별하는 것 중요
# board를 만들어서 따로 계산하기
