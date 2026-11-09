from collections import deque
def solution(m, n, h, w, drops):
    INF = len(drops) + 1
    rain = [[INF]*n for _ in range(m)]
    
    for i, (r,c) in enumerate(drops,1):
        rain[r][c] = i
        
    width = n - w + 1
    row_min = [[0]*width for _ in range(m)]
    
    for r in range(m):
        queue = deque()
        for c in range(n):
            while queue and rain[r][queue[-1]] >= rain[r][c]:
                queue.pop()
            queue.append(c)
            
            if queue[0] <= c - w:
                queue.popleft()
            
            if c >= w - 1:
                row_min[r][c-w+1] = rain[r][queue[0]]
    
    answer = [0,0]
    best = -1
    
    for c in range(width):
        queue = deque()
        for r in range(m):
            while queue and row_min[queue[-1]][c] >= row_min[r][c]:
                queue.pop()
            
            queue.append(r)
            
            if queue[0] <= r - h:
                queue.popleft()
            
            if r >= h - 1:
                value = row_min[queue[0]][c]
                start_r = r - h + 1
                
                if value > best or (value == best and (start_r,c) < (answer[0],answer[1])):
                    best = value
                    answer = [start_r, c]
                    
    return answer

## 풀이전략, 핵심 아이디어
# 2차원 슬라이딩 윈도우 활용
# 모든 직사각형을 하나씩 검사하지 않고, 직사각형 내부의 최솟값을 빠르게 구하는 것이 핵심
