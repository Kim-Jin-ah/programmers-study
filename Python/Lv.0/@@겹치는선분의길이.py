def solution(lines):
    answer = 0
    line_map = {}
    
    for line in lines:
        for i in range(line[0],line[1]):
            line_map[i] = line_map.get(i,0) + 1
            
    for count in line_map.values():
        if count >= 2:
            answer += 1
            
    return answer

## 풀이전략, 핵심 아이디어
# 수직전의 각 위치를 기록하기 위해 딕셔너리 사용
# 선분 시작부터 끝까지 한번 지나갔으면 +1
# 이때, +2 이상인 부분이 있다면 answer에 +1
