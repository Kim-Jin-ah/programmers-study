def solution(grid):
    n = len(grid)
    m = len(grid[0])
    
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    visited = [[[False]*4 for _ in range(m)] for _ in range(n)]
    
    answer = []
    for i in range(n):
        for j in range(m):
            for d in range(4):
                if visited[i][j][d]:
                    continue
                    
                x,y = i,j
                direction = d
                count = 0
                
                while not visited[x][y][direction]:
                    visited[x][y][direction] = True
                    count += 1
                    
                    if grid[x][y] == "L":
                        direction = (direction - 1) % 4
                    elif grid[x][y] == "R":
                        direction = (direction + 1) % 4
                    x = (x + dx[direction]) % n
                    y = (y + dy[direction]) % m
                
                answer.append(count)
                
    return sorted(answer)

## 풀이전략, 핵심 아이디어
# 3차원 방문 배열을 사용해야하는 문제
# %를 사용하여, 방향 변경 + 격자 끝에서 반대편으로 이동 식 만들기
