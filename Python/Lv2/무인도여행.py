from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    maps = [list(row) for row in maps]
    answer = []
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "X":
                continue
            queue = deque([(i,j)])
            
            value = int(maps[i][j])
            maps[i][j] = "X"
            
            total = value
            
            while queue:
                x,y = queue.popleft()
                for dx,dy in directions:
                    nx = x + dx
                    ny = y + dy
                    
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue
                    if maps[nx][ny] == "X":
                        continue
                        
                    total += int(maps[nx][ny])
                    maps[nx][ny] = "X"
                    queue.append((nx,ny))
            answer.append(total)
            
    if not answer:
        return [-1]

    return sorted(answer)

## 풀이전략, 핵심 아이디어
# 기존 BFS 문제의 심화 버전. dequeue 사용과 값 누적 신경쓰기
