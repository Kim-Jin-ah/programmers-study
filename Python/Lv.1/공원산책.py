def solution(park, routes):
    answer = []
    direction = {"N":(-1,0), "S":(1,0), "W":(0,-1), "E":(0,1)}
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                x,y = i,j
    
    for route in routes:
        d,n = route.split()
        n = int(n)
        
        dx,dy = direction[d]
        nx = x
        ny = y
        possible = True
        
        for _ in range(n):
            nx += dx
            ny += dy
            
            if nx < 0 or nx >= len(park) or ny < 0 or ny >= len(park[0]):
                possible = False
                break
            if park[nx][ny] == "X":
                possible = False
                break
        if possible:
            x = nx
            y = ny
    
    return [x,y]

## 풀이전략, 핵심 아이디어
# 현재 위치 저장 -> 방향별 이동량 준비 -> 명령마다 임시위치를 사용해 한칸씩 이동 -> 이동 중 범위나 장애물을 만나면 취소 -> 끝까지 성공하면 현재 위치 갱신
# 진짜 어렵다,,,,그냥 외워,,
