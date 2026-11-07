def solution(m, n, startX, startY, balls):
    answer = []
    for x,y in balls:
        distances = []
        
        if not (startY == y and startX > x):
            distances.append((startX + x)**2 + (startY - y)**2)
        
        if not (startY == y and startX < x):
            distances.append((2*m - startX - x)**2 + (startY - y)**2)
            
        if not (startX == x and startY > y):
            distances.append((startX - x)**2 + (startY + y)**2)
            
        if not (startX == x and startY < y):
            distances.append((startX-x)**2 + (2*n - startY - y)**2)
            
        answer.append(min(distances))
        
    return answer

## 풀이전략, 핵심 아이디어
# 대칭이동으로 벽에 튕기는 경로를 직선 경로로 바꾼다
# 거리 제곱을 해야하기 때문에 **2만 사용하고 제곱근은 구하지 않는다
# 벽에 도달하기 전에 목적지 공을 먼저 지나가는 경로를 제외하여 예외처리를 한다.
