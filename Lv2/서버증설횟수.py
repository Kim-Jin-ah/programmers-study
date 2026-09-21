def solution(players, m, k):
    server = [0] * (len(players) + k)
    answer = 0
    current = 0
    
    for i in range(len(players)):
        if i >= k:
            current -= server[i-k]
        
        need = players[i] // m
        
        if current < need:
            add = need - current
            
            server[i] += add
            current += add
            answer += add
            
    return answer

## 풀이전략, 핵심 아이디어
# 현재 시간의 이용자 수 -> 필요한 서버 계산 -> 현재 살아있는 서버와 비교 -> 부족하면 증설 -> 증설한 서버를 server[i]에 기록 -> k시간 후 server[i-k]를 빼서 만료 처리
