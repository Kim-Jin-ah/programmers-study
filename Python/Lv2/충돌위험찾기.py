def solution(points, routes):
    paths = []
    for route in routes:
        r,c = points[route[0]-1]
        path = [(r,c)]
        
        for p in route[1:]:
            nr,nc = points[p-1]
            
            while r != nr:
                if r < nr:
                    r += 1
                else:
                    r -= 1
                path.append((r,c))
                
            while c != nc:
                if c < nc:
                    c += 1
                else:
                    c -= 1
                path.append((r,c))
        paths.append(path)
        
    answer = 0
    max_time = max(len(path) for path in paths)
    
    for t in range(max_time):
        positions = {}
        for path in paths:
            if t < len(path):
                pos = path[t]
                positions[pos] = positions.get(pos,0) + 1
        for count in positions.values():
            if count >= 2:
                answer += 1
    
    return answer

## 풀이전략, 핵심 아이디어
# 로봇별 이동 경로 생성(r이동->c이동->좌표저장)
# 시간별 로봇 위치 확인(각 로봇의 t번째 좌표 확인)
# 좌표별 로봇 수 계산(같은 좌표에 2대 이상인지 확인)
# 위험 상황 총 횟수 반환(위험한 좌표가 발견될 때마다 1회 추가)
