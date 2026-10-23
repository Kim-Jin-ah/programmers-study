def solution(dirs):
    x,y = 0,0
    visited = set()
    
    for command in dirs:
        nx,ny = x,y
        
        if command == "U":
            ny += 1
        elif command == "D":
            ny -= 1
        elif command == "R":
            nx += 1
        elif command == "L":
            nx -= 1
        
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
            
        if ((x,y),(nx,ny)) not in visited:
            visited.add(((x,y),(nx,ny)))
            visited.add(((nx,ny),(x,y)))
            
        x,y = nx,ny
    
    return len(visited) // 2

## 풀이전략, 핵심 아이디어
# 방문한 좌표를 저장하는 것이 아닌 방문한 길을 저장해야 한다 가 핵심!
# 현재위치 확인 후 다음 위치 계산 -> 범위 안인지 확인 -> 새로운 길인지 확인 -> 맞다면 길 저장 -> 현재 위치를 다음 위치로 변경
