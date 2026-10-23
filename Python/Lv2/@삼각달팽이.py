def solution(n):
    answer = [[0]*n for _ in range(n)]
    
    x = 0
    y = 0
    number = 1
    directions = [(1,0),(0,1),(-1,-1)]
    
    direction = 0
    for _ in range(n*(n+1) // 2):
        answer[x][y] = number
        number += 1
        
        nx = x + directions[direction][0]
        ny = y + directions[direction][1]
        
        if (nx < 0 or nx >= n or ny < 0 or ny >= n or answer[nx][ny] != 0):
            direction = (direction+1) % 3
            
            nx = x + directions[direction][0]
            ny = y + directions[direction][1]
        
        x = nx
        y = ny
    
    return [num for row in answer for num in row if num != 0]

## 풀이전략, 핵심 아이디어
# directions의 세 방향 설정 후 반복문 안에서 어떤 상황일 때 방향이 바뀌는지 넣고, 0을 제외한 배열 return
# 삼각형으로 배열이 돌아가는 과정과 방향 잘 익히기
