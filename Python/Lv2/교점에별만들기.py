def solution(line):
    points = []
    n = len(line)
    
    for i in range(n):
        for j in range(i+1,n):
            a1,b1,c1 = line[i]
            a2,b2,c2 = line[j]
            det = a1*b2 - a2*b1
            
            if det == 0:
                continue
            
            x_num = b1*c2 - b2*c1
            y_num = c1*a2 - c2*a1
            
            if x_num % det == 0 and y_num % det == 0:
                x = x_num // det
                y = y_num // det
                points.append((x,y))
                
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)            
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    
    grid = [['.']*width for _ in range(height)]
    
    for x,y in points:
        grid[max_y - y][x - min_x] = '*'
        
    return ["".join(row) for row in grid]

## 풀이전략, 핵심 아이디어
# 이중 for문으로 모든 직선의 쌍을 비교하여 교점 구하기
# 교점이 정수인지 if문으로 확인
# y축 인덱스를 뒤집어 반환
