def solution(cap, n, deliveries, pickups):
    answer = 0
    d = 0
    p = 0
    
    for i in range(n-1,-1,-1):
        d += deliveries[i]
        p += pickups[i]
        
        while d > 0 or p > 0:
            answer += (i+1) * 2
            d -= cap
            p -= cap
            
    return answer

## 풀이전략, 핵심 아이디어
# 가장 먼 집부터 배달과 수거의 누적량을 각각 관리하고
# 둘 중 하나라도 남아있다면 트럭용량만큼 처리할 수 있는 왕복횟수 추가
